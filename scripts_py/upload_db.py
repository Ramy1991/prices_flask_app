import mysql.connector
from mysql.connector import errorcode
import json
import uuid
from hashlib import blake2b
import langid
from datetime import datetime, date

data = {
    "AM423MW0Y209WNAFAMZ": {
        "item_title": "American Eagle Graphic T-Shirt - Burgundy",
        "item_image": "https://eg.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/57/200612/1.jpg?4544",
        "item_url": "https://www.jumia.com.eg/american-eagle-graphic-t-shirt-burgundy-21600275.html",
        "item_price": "164.00",
        "item_uid": "AM423MW0Y209WNAFAMZ",
        "product_type": "Sports Wear @ Shirts & Tees",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:48",
        "item_website": "www.jumia.com.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": "",
        "brand": "",
        "item_title_ar": "American Eagle Graphic T-Shirt - Burgundy",
        "product_type_ar": "ملابس رياضية رجالي @ تي شيرتات",
        "item_url_ar": "https://www.jumia.com.eg/ar/american-eagle-graphic-t-shirt-burgundy-21600275.html",
        "brand_ar": "",
        "search_value": "shirts"
    },
    "B08Y8Z25KL": {
        "item_title": "Carina Cotton Basic Short Sleeves Under Shirt for Women, Select",
        "item_image": "https://m.media-amazon.com/images/I/31qYmuuGHuS._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B08Y8Z25KL/?language=en_AE",
        "item_price": "74.",
        "item_uid": "B0994ZFZG6",
        "product_type": "Women's Activewear Undershirts",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:48",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": {
            "S": "found",
            "M": "found",
            "L": "found",
            "XL": "found",
            "XXL": "found"
        },
        "brand": "Carina",
        "item_title_ar": "Carina Cotton Basic Short Sleeves Under Shirt for Women",
        "product_type_ar": "Women's Activewear Undershirts",
        "item_url_ar": "https://www.amazon.eg/dp/B08Y8Z25KL/?language=en_AE",
        "brand_ar": "Carina",
        "search_value": "shirts"
    },
    "B08YNSG784": {
        "item_title": "T-Shirts V Neck Cotton Men summer - 5X, Select",
        "item_image": "https://m.media-amazon.com/images/I/41S12jfKJfL._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B08YNSG784/?language=en_AE",
        "item_price": "34.",
        "item_uid": "B08YP6C88T",
        "product_type": "Tops, Tees & Shirts @ T-Shirts @ Men's T-Shirts",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:48",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": {
            "L": "found"
        },
        "brand": "Generic",
        "item_title_ar": "T-Shirts V Neck Cotton Men summer - 5X",
        "product_type_ar": "Tops, Tees & Shirts @ T-Shirts @ Men's T-Shirts",
        "item_url_ar": "https://www.amazon.eg/dp/B08YNSG784/?language=en_AE",
        "brand_ar": "Generic",
        "search_value": "shirts"
    },
    "B091J7QBJD": {
        "item_title": "Hero EG White Mixed V Neck T-Shirt For Men",
        "item_image": "https://m.media-amazon.com/images/I/3104d5SqkML._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B091J7QBJD/?language=en_AE",
        "item_price": "54.",
        "item_uid": "B091J7QBJD",
        "product_type": "Tops, Tees & Shirts @ T-Shirts @ Men's T-Shirts",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:48",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": "",
        "brand": "Hero EG",
        "item_title_ar": "Hero EG White Mixed V Neck T-Shirt For Men",
        "product_type_ar": "Tops, Tees & Shirts @ T-Shirts @ Men's T-Shirts",
        "item_url_ar": "https://www.amazon.eg/dp/B091J7QBJD/?language=en_AE",
        "brand_ar": "Hero EG",
        "search_value": "shirts"
    },
    "B09693H637": {
        "item_title": "Print.Online T-Shirts For women -white - 2724631318850, Select",
        "item_image": "https://m.media-amazon.com/images/I/413Fjn-kZnS._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B09693H637/?language=en_AE",
        "item_price": "119.",
        "item_uid": "B092PW3CR9",
        "product_type": "",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:49",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": {
            "M": "found",
            "L": "found",
            "X-Large": "found",
            "XXL": "found"
        },
        "brand": "Print.Online",
        "item_title_ar": "Print.Online T-Shirts For women -white - 2724631318850",
        "product_type_ar": "",
        "item_url_ar": "https://www.amazon.eg/dp/B09693H637/?language=en_AE",
        "brand_ar": "Print.Online",
        "search_value": "shirts"
    },
    "B08YNPP65R": {
        "item_title": "T-Shirts Round Neck Cotton Men summer 5X, Select",
        "item_image": "https://m.media-amazon.com/images/I/41J+xeuJraL._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B08YNPP65R/?language=en_AE",
        "item_price": "34.",
        "item_uid": "B08YNSMZS4",
        "product_type": "Men's T-Shirts",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:49",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": {
            "L": "found"
        },
        "brand": "Generic",
        "item_title_ar": "T-Shirts Round Neck Cotton Men summer 5X",
        "product_type_ar": "Men's T-Shirts",
        "item_url_ar": "https://www.amazon.eg/dp/B08YNPP65R/?language=en_AE",
        "brand_ar": "Generic",
        "search_value": "shirts"
    },
    "B091JMWQCF": {
        "item_title": "Soko Mesh Men's Shirt Stays Adjustable Shirt Holders Crease-Resistance Belt Stirrup Style Suspenders",
        "item_image": "https://m.media-amazon.com/images/I/41mJeiaCiiL._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B091JMWQCF/?language=en_AE",
        "item_price": "101.",
        "item_uid": "B091JMWQCF",
        "product_type": "Cufflinks & Shirt Accessories @ Men's Cufflinks & Shirt Accessories",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:49",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": "",
        "brand": "Soko Mesh",
        "item_title_ar": "Soko Mesh Men's Shirt Stays Adjustable Shirt Holders Crease-Resistance Belt Stirrup Style Suspenders",
        "product_type_ar": "Cufflinks & Shirt Accessories @ Men's Cufflinks & Shirt Accessories",
        "item_url_ar": "https://www.amazon.eg/dp/B091JMWQCF/?language=en_AE",
        "brand_ar": "Soko Mesh",
        "search_value": "shirts"
    },
    "B09233DTXH": {
        "item_title": "Cottonil Combed Under Shirt - Set of 3 Hlaf Sleeves Under shirts - 100% Cotton - for Men, Select",
        "item_image": "https://m.media-amazon.com/images/I/21mheyo7k1S._AC_SR38,50_.jpg",
        "item_url": "https://www.amazon.eg/dp/B09233DTXH/?language=en_AE",
        "item_price": "135.",
        "item_uid": "B091JLRFFB",
        "product_type": "Men's Activewear Undershirts",
        "currency": "EGP",
        "date": "18-09-2021",
        "time": "20:30:49",
        "item_website": "www.amazon.eg",
        "country": "eg",
        "tree": "",
        "item_sizes": {
            "2X": "found",
            "M": "found",
            "L": "found",
            "XL": "found"
        },
        "brand": "Cottonil",
        "item_title_ar": "Cottonil Combed Under Shirt - Set of 3 Hlaf Sleeves Under shirts - 100% Cotton - for Men",
        "product_type_ar": "Men's Activewear Undershirts",
        "item_url_ar": "https://www.amazon.eg/dp/B09233DTXH/?language=en_AE",
        "brand_ar": "Cottonil",
        "search_value": "shirts"
    }
}


class UploadDB:
    def __init__(self, json_data):
        self.json_items = json_data
        self.new_product = []
        self.existed_products = {}
        self.products_to_update = []
        self.currency = self.json_items.get(next(iter(self.json_items))).get('currency')
        self.country = self.json_items.get(next(iter(self.json_items))).get('country')
        # next(iter(self.json_items))

    def db_connection(self):
        try:
            conn = mysql.connector.connect(user="admin", password="PTS-0000",
                                           host="130.162.40.58", port=3306, database="main_schema")
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
        FROM main_schema.products_{self.country} WHERE source_identifier_code in {SIC_list};"""
        # ', '.join(map(str, rows))
        connection = self.db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(check_query)

        self.existed_products = {item.get('source_identifier_code'): item for item in cursor.fetchall()}
        print(self.existed_products)

    def extract_json(self):
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
                        item.get('item_title'),
                        item.get('item_title_ar'),
                        item.get('brand'),
                        item.get('brand_ar'),
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
                        item.get('item_title'),
                        item.get('item_title_ar'),
                        item.get('brand'),
                        item.get('brand_ar'),
                        item.get('item_image'),
                        item.get('item_url'),
                        item.get('item_url_ar'),
                        0 if item_price else 1,
                        str(date.today().strftime("%y-%m-%d")),
                        SIC
                    ]
                    self.products_to_update.append(tuple(item_list))

    def execute_query(self, query, values):
        connection = self.db_connection()
        cursor = connection.cursor()

        try:
            cursor.executemany(query, values)
            connection.commit()
            return len(values)
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
        results_add = ''
        results_update = ''
        if len(self.new_product) != 0:
            print(insert_query)
            results_add = self.execute_query(insert_query, self.new_product)
        if len(self.products_to_update) != 0:
            results_update = self.execute_query(update_query, self.products_to_update)

        return f'Added: {results_add}__ Updated: {results_update}'


# ex = UploadDB(data).main()
# print(ex)

# h = blake2b(digest_size=2)
# tes = 'ramy'
# h.update(tes.encode("utf-8"))
# #
# #
# print(h.hexdigest() + str(uuid.uuid4())[:4])
