import mysql.connector
from mysql.connector import errorcode
import json
from scripts_py.supported_website import country_alpha2_currency
import re


class ProductPage:
    def __init__(self, country, lang, search_value):
        self.country = country
        self.lang = lang
        self.items_results = {}
        self.search_value = search_value

    def query(self, query, item_uid, item_type):
        item_query = {
            'query_item':
                f"SELECT website_name, UIC, unique_product_code, title_{self.lang} as item_title, brand_{self.lang}, "
                f"images_url, item_type_{self.lang} as item_type, sub_category_{self.lang}, "
                f"item_upc, product_direct_link_{self.lang} as product_direct_link "
                f", rating, number_of_reviews, "
                f"JSON_EXTRACT(price_data->>'$.egp.*', "
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) as price,"
                f" item_specs_{self.lang} as item_specs, country "
                f"FROM main_schema.products_{self.country} WHERE UIC = '{self.search_value}' "
                f"AND country = '{self.country}';",
            'matching_items_query':
                f"SELECT website_name, UIC, unique_product_code, title_{self.lang} as item_title, brand_{self.lang}, "
                f"images_url, item_type_{self.lang} as item_type, sub_category_{self.lang}, "
                f"item_upc, product_direct_link_{self.lang} as product_direct_link "
                f", rating, number_of_reviews, "
                f"JSON_EXTRACT(price_data->>'$.egp.*', "
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) as price, country "
                f"FROM main_schema.products_{self.country} WHERE "
                f"MATCH(title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE ) "
                f"AND country = '{self.country}' AND UIC != '{item_uid}' AND  "
                f"item_type_{self.lang} = '{item_type}' LIMIT 4;"

        }
        return item_query.get(query)

    def trim_item_specs_json(self, specs):
        trim_specs = specs.replace('class="fi-x"', "class='fi-x'").replace('class="clearfix"', "class='clearfix'") \
            .replace('class="fi-check"', "class='fi-check'").replace('""', '"')
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
            cursor.execute(self.query('query_item', '', ''))  # execute query
            item_result = cursor.fetchone()
            if item_result:
                # reformat price
                item_result['price'] = '{:,.2f}'.format(float(item_result['price'].replace('"', '')))
                # reformat json
                item_result['item_specs'] = json.loads(self.trim_item_specs_json(item_result['item_specs']))
                # get main image
                item_result['images_url'] = item_result['images_url'].split('\n')[0]
                # add currency
                currency = {'currency': country_alpha2_currency[item_result['country'].upper()]['currency']}
                item_result.update(currency)
                # set link

                item_title = re.sub(r"[&\/\\#,+()$~%.'':*?<>{}!@\s\"]", '-', item_result['item_title'])
                item_title = re.sub(r"[-]+", '-', item_title)
                item_type = re.sub(r"[&\/\\#,+()$~%.'':*?<>{}!@\s\"]", '-', item_result['item_type'])
                item_type = re.sub(r"[-]+", '-', item_type)
                item_result['item_link'] = '{}/{}/{}'.format(item_type, item_title, item_result['UIC']).lower()

                self.items_results = item_result

                # get similar items
                self.search_value = item_result.get('item_title')

                cursor.execute(self.query('matching_items_query', item_result.get('UIC'), item_result['item_type']))
                similar_items = cursor.fetchall()

                self.items_results = {'item_data': item_result, 'similar_items': similar_items}

                return json.dumps(self.items_results)
            else:
                return json.dumps({'Error item not found': self.search_value})


# print(ProductPage('eg', 'en', 'A6f98a11fe').db_connection())
