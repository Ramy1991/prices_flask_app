import mysql.connector
from mysql.connector import errorcode
import json


#
class DBSearch(object):

    def __init__(self, search_value, country, lang):
        self.search_value = search_value
        self.country = country
        self.lang = lang
        self.items_dict_search = {}

    def search_query(self):
        query = f"WITH r AS (SELECT  website_name, UIC, unique_product_code, title_{self.lang}, brand_{self.lang}," \
                f" images_url, item_tybe_{self.lang}, sub_category_{self.lang}, item_upc, link_{self.lang}, " \
                f"product_direct_link_{self.lang}, rating, " \
                f"number_of_reviews, JSON_EXTRACT(price_data->>'$.egp.*', " \
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) " \
                f"FROM products WHERE item_tybe_en = (" \
                f"SELECT item_tybe_en FROM search_mapping WHERE " \
                f"MATCH(search_key_s) against('+{self.search_value}' IN NATURAL LANGUAGE MODE) " \
                f"order by search_order ASC limit 1" \
                f") AND MATCH(title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE ) AND" \
                f" JSON_EXTRACT(price_data->>'$.egp.*', " \
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None' AND" \
                f" sold_out = 0 AND country like '%{self.country}%' LIMIT 60)" \
                f" SELECT * FROM r " \
                f"UNION ALL" \
                f" SELECT  website_name, UIC, unique_product_code, title_{self.lang}, brand_{self.lang}, " \
                f"images_url, item_tybe_{self.lang}, sub_category_{self.lang}," \
                f"item_upc, link_{self.lang}, product_direct_link_{self.lang}, rating, number_of_reviews, " \
                f"JSON_EXTRACT(price_data->>'$.egp.*', " \
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) " \
                f"FROM products WHERE " \
                f"MATCH(title_{self.lang}) against('+{self.search_value}' IN BOOLEAN MODE ) " \
                f"AND JSON_EXTRACT(price_data->>'$.egp.*', " \
                f"CONCAT('$[',JSON_LENGTH(price_data->>'$.egp.*.price')-1,'].price')) != 'None'" \
                f"AND sold_out = 0 AND country like '%{self.country}%' AND NOT EXISTS (SELECT * FROM r) LIMIT 60;"
        return query

    def db_connection(self):
        try:
            conn = mysql.connector.connect(user="admin", password="Api-0000",
                                           host="8.9.3.120", port=3306, database="main_schema")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute(self.search_query())
            result = cursor.fetchall()
            items_dict_search = {}
            for item in result:
                if item[0] not in items_dict_search:
                    items_dict_search = {
                        item[0]: {  # store
                        }
                    }
                item_dict_search = {
                    item[2]: {  # item_uid
                        "website_name": item[0],  #
                        "item_uid": item[1],
                        "unique_product_code": item[2],  #
                        "item_title": item[3],
                        "brand_en": item[4],  #
                        "item_image": item[5].split('\n')[0],
                        "item_tybe_en": item[6],  #
                        "sub_category_en": item[7],  #
                        "item_upc": item[8],  #
                        "link_en": item[9],  #
                        "item_url": item[10],
                        "rating": item[11],  #
                        "number_of_reviews": item[12],  #
                        "item_price": '{:,.2f}'.format(float(item[13].replace('"', ''))),

                    }
                }
                items_dict_search[item[0]].update(item_dict_search)
            self.items_dict_search = json.dumps([items_dict_search])
            return self.items_dict_search

# print(DBSearch('iphone', 'eg', 'en').db_connection())
