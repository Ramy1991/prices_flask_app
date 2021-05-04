import mysql.connector
from mysql.connector import errorcode
import json


#
class DBSearch(object):

    def __init__(self, search_value):
        self.search_value = search_value
        self.items_dict_search = {}

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
            cursor.execute(
                "SELECT website_name, title_en, title_ar, unique_product_code, link_en, price_data, images_url, "
                "brand_en, brand_ar, item_type_en, item_type_ar, UIC, link_ar, item_upc, product_direct_link_en,"
                "product_direct_link_ar FROM products WHERE MATCH(title_en) "
                "against('%{}%' IN NATURAL LANGUAGE MODE) "
                "AND country like '%eg%' LIMIT 30".format(self.search_value))
            result = cursor.fetchall()
            items_dict_search = {}
            for item in result:
                if item[0] not in items_dict_search:
                    items_dict_search = {
                        item[0]: {  # store
                        }
                    }
                item_dict_search = {
                    item[3]: {  # item_uid
                        "item_title": item[1],
                        "item_title_AR": item[2],
                        "item_image": item[6].split("\n")[0],
                        "item_price": item[5],
                        "item_url": item[14],
                        "item_url_ar": item[15],
                        "item_uid": item[3],
                        "search_key": self.search_value
                    }
                }
                items_dict_search[item[0]].update(item_dict_search)
            self.items_dict_search = json.dumps([items_dict_search])
            return self.items_dict_search


print(DBSearch('iphone').db_connection())
