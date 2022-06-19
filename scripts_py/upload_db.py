import mysql.connector
from mysql.connector import errorcode
import json
import uuid
from hashlib import blake2b
import langid
from datetime import datetime, date
import re
from scripts_py.supported_website import country_alpha2_currency


class UploadDB:
    def __init__(self, json_data, country, search_value):
        self.json_items = json_data
        self.new_product = []
        self.existed_products = {}
        self.products_to_update = []
        self.currency = country_alpha2_currency.get(country.upper()).get('currency')
        self.country = country
        self.search_value = search_value
        # next(iter(self.json_items))

    def db_infos(self, server_name):
        db_servers = {
            'oracle': {
                'user': 'admin',
                'password': 'PTS-0000',
                'host': '130.162.40.58',
                'database': 'main_schema'
            },
            'pscale': {
                'user': 'mmk4m1fm109k',
                'password': 'pscale_pw_YHKalJ1HnIt2TKbSsKWNEAwpuMtV_WxBBlf2_qlHCKk',
                'host': 'rpdfka86np0m.eu-central-2.psdb.cloud',
                'database': 'main_schema'
            }
        }
        return db_servers.get(server_name)

    def db_connection(self, db_info):
        try:
            conn = mysql.connector.connect(user=db_info.get('user'), password=db_info.get('password'),
                                           host=db_info.get('host'), port=3306, database=db_info.get('database'))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(f"ERROR {err}")
        else:
            return conn

    def UID_Generator(self, unique_product_code):
        text_hash = blake2b(digest_size=2)
        text_hash.update(unique_product_code.encode("utf-8"))
        return f"A{text_hash.hexdigest()}{str(uuid.uuid4())[:4]}"

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', str(text))

    def search_key_lang(self):
        search_value = list(self.json_items.values())[0].get('search_value')
        search_key_lang = langid.classify(search_value)[0]
        if search_key_lang == 'en':
            return 'search_key'
        elif search_key_lang == 'ar':
            return 'search_key_ar'
        else:
            return 'search_key'

    def check_duplicate(self):
        SIC_list = tuple(self.json_items.keys())
        check_query = f"""SELECT source_identifier_code, JSON_EXTRACT(JSON_EXTRACT(price_data, '$.{self.currency}.*'), 
        CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.{self.currency}.*'))-1,'].price')) as price 
        FROM main_schema.products_eg WHERE source_identifier_code in {SIC_list};"""
        # ', '.join(map(str, rows))

        connection = self.db_connection(self.db_infos('oracle'))
        cursor = connection.cursor(dictionary=True)
        if SIC_list:
            cursor.execute(check_query)

        self.existed_products = {item.get('source_identifier_code'): item for item in cursor.fetchall()}
        # print(self.existed_products)

    def extract_json(self):
        r = 1
        for SIC, item in self.json_items.items():
            if 'missing_data' not in item.values():
                item_price = item.get('item_price').replace(',', '.')
                price_dict = {
                    item.get('currency'): {
                        f'{item.get("date")}_{item.get("time")}': {
                            'date_time': f'{item.get("date")} {item.get("time")}',
                            'price': float(item_price),
                            'currency': item.get('currency')
                        }
                    }
                }
                # print(f"{self.existed_products.get(SIC).get('price')}: {float(item.get('item_price'))}")
                # print(self.existed_products.get(SIC).get('price'))
                if not self.existed_products.get(SIC):
                    # print(str(r) + ' ' + item.get('item_title'))
                    item_list = [
                        SIC,
                        item.get('item_website'),
                        self.UID_Generator(SIC),
                        item.get('country'),
                        json.dumps(price_dict),
                        item.get('product_type'),
                        item.get('product_type_ar'),
                        item.get('product_type').split(' @ ')[-1],
                        item.get('product_type_ar').split(' @ ')[-1],
                        item.get('search_value'),
                        item.get('item_title')[:200],
                        item.get('item_title_ar')[:200],
                        self.clean_text(item.get('brand')),
                        self.clean_text(item.get('brand_ar')),
                        '',
                        '',
                        item.get('item_image'),
                        item.get('item_url'),
                        item.get('item_url_ar'),
                        '',
                        0 if item_price else 1,
                        0,
                        0,
                        str(date.today().strftime("%y-%m-%d"))
                    ]
                    self.new_product.append(tuple(item_list))

                elif float(self.existed_products.get(SIC).get('price').replace('"', '')) != float(item_price):
                    # print(str(r) + ' ' + item.get('item_title'))
                    item_list = [
                        f'$.{item.get("currency")}."{item.get("date")}_{item.get("time")}"',
                        float(item_price),
                        item.get('currency'),
                        f'{item.get("date")}_{item.get("time")}',
                        # json.dumps(price_dict),
                        item.get('search_value'),
                        item.get('product_type'),
                        item.get('product_type_ar'),
                        item.get('product_type').split(' @ ')[-1],
                        item.get('product_type_ar').split(' @ ')[-1],
                        item.get('item_title')[:200],
                        item.get('item_title_ar')[:200],
                        self.clean_text(item.get('brand')),
                        self.clean_text(item.get('brand_ar')),
                        item.get('item_image'),
                        item.get('item_url'),
                        item.get('item_url_ar'),
                        0 if item_price else 1,
                        str(date.today().strftime("%y-%m-%d")),
                        SIC
                    ]
                    self.products_to_update.append(tuple(item_list))
                r += 1

    def execute_query(self, connection, query, values):
        # connection = self.db_connection()
        cursor = connection.cursor()
        try:
            if values:
                cursor.executemany(query, values)
                connection.commit()
                # connection.close()
                return len(values)
            else:
                cursor.execute(query)
                connection.commit()
                # connection.close()
                return True
        except Exception as err:
            return err

    def main(self):
        # check Duplicate before Upload
        self.check_duplicate()
        # group item based on new products and the products need to update
        self.extract_json()
        # check for list of that needs to add or update
        insert_query = f"""INSERT INTO products_eg (source_identifier_code, website_name, UIC, country, price_data, 
                            product_category_en, product_category_ar, product_type_en, product_type_ar, 
                            {self.search_key_lang()}, title_en, title_ar, brand_en, brand_ar, item_specs_en, 
                            item_specs_ar, images_url, product_direct_link_en, product_direct_link_ar, item_upc, 
                            sold_out, rating, number_of_reviews, item_date) VALUES 
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                            %s, %s, %s);"""
        update_query = f"""UPDATE main_schema.products_eg SET 
                            `price_data` = JSON_INSERT(`price_data`, %s,
                                JSON_OBJECT("price", %s, "currency", %s, "date_time", %s)
                        ), {self.search_key_lang()} = CONCAT(search_key,' # ', %s), product_category_en = %s, 
                        product_category_ar = %s, product_type_en = %s, product_type_ar = %s, title_en = %s, 
                        title_ar = %s, brand_en = %s, brand_ar = %s, images_url = %s, product_direct_link_en = %s, 
                        product_direct_link_ar = %s, sold_out = %s, item_date = %s
                        WHERE source_identifier_code = %s ;"""
        # create connection for two servers
        connection_1 = self.db_connection(self.db_infos('oracle'))
        connection_2 = self.db_connection(self.db_infos('pscale'))

        results_add = ''
        results_update = ''
        if len(self.new_product) != 0:
            results_add = self.execute_query(connection_1, insert_query, self.new_product)
            results_add_2 = self.execute_query(connection_2, insert_query, self.new_product)
        if len(self.products_to_update) != 0:
            results_update = self.execute_query(connection_1, update_query, self.products_to_update)
            results_update_2 = self.execute_query(connection_2, update_query, self.products_to_update)

        # update the status
        st_query = f"""INSERT INTO update_db_user_search (search_value, num_of_uploaded, num_of_updated, 
                    search_date, country) VALUES('{self.search_value}', '{str(results_add)}', '{str(results_update)}', 
                    '{str(date.today().strftime("%y-%m-%d"))}', '{self.country}');"""

        results_update = self.execute_query(connection_1, st_query, [])

        self.execute_query(connection_2, st_query, [])

        return f'Added: {results_add}__ Updated: {results_update}'

# ex = UploadDB(data).main()
# print(ex)

# h = blake2b(digest_size=2)
# tes = 'ramy'
# h.update(tes.encode("utf-8"))
# #
# #
# print(h.hexdigest() + str(uuid.uuid4())[:4])
