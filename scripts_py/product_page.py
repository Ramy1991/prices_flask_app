import mysql.connector
from mysql.connector import errorcode
import json
from scripts_py.supported_website import country_alpha2_currency
import re


class ProductPage(object):
    def __init__(self, country, lang, search_value):
        self.country = country
        self.lang = lang
        self.items_results = {}
        self.search_value = search_value

    def query(self):
        item_query = {
            'query':
                f"SELECT website_name, UIC, unique_product_code, title_{self.lang} as item_title, brand_{self.lang}, "
                f"images_url, item_type_{self.lang} as item_type, sub_category_{self.lang}, "
                f"item_upc, link_{self.lang} as item_link, product_direct_link_{self.lang} as product_direct_link "
                f", rating, number_of_reviews, "
                f"JSON_EXTRACT(price_data->>'$.egp.*', "
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) as price,"
                f" item_specs_{self.lang} as item_specs, country "
                f"FROM main_schema.products WHERE UIC = '{self.search_value}' AND country = '{self.country}';"
        }
        return item_query.get('query')

    def trim_item_specs_json(self, specs):
        trim_specs = specs.replace('class="fi-x"', "class='fi-x'").replace('class="clearfix"', "class='clearfix'") \
            .replace('class="fi-check"', "class='fi-check'")
        return trim_specs

    def db_connection(self):
        try:
            conn = mysql.connector.connect(user="admin", password="Api-0000",
                                           host="134.122.93.25", port=3306, database="main_schema")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(self.query())  # execute query
            result = cursor.fetchone()
            # reformat price
            result['price'] = '{:,.2f}'.format(float(result['price'].replace('"', '')))
            # reformat json
            result['item_specs'] = json.loads(self.trim_item_specs_json(result['item_specs']))
            # get main image
            result['images_url'] = result['images_url'].split('\n')[0]
            # add currency
            currency = {'currency': country_alpha2_currency[result['country'].upper()]['currency']}
            result.update(currency)
            # set link
            item_type = re.sub(r"[&\/\\#,+()$~%.'':*?<>{}!@\s\"]", '-', result['item_type'])
            item_title = re.sub(r"[&\/\\#,+()$~%.'':*?<>{}!@\s\"]", '-', result['item_title'])
            item_title = re.sub(r"[-]+", '-', item_title)
            result['item_link'] = '{}/{}/{}'.format(item_type, item_title, result['UIC']).lower()

            self.items_results = result
            # self.items_results = {  # item_uida
            #     'website_name': result[0],  #
            #     'item_uid': result[1],
            #     'unique_product_code': result[2],  #
            #     'item_title': result[3],
            #     'brand_en': result[4],  #
            #     'item_image': result[5].split('\n')[0],
            #     'item_type_en': result[6],  #
            #     'sub_category_en': result[7],  #
            #     'item_upc': result[8],  #
            #     'link_en': result[9],  #
            #     'item_url': result[10],
            #     'rating': result[11],  #
            #     'number_of_reviews': result[12],  #
            #     'item_price': '{:,.2f}'.format(float(result[13].replace('"', ''))),
            #     'item_specs': json.loads(self.trim_item_specs_json(result[14]))
            # }

            return json.dumps(self.items_results)


# print(ProductPage('eg', 'en', 'A365d591e0').db_connection())
