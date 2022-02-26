import mysql.connector
from mysql.connector import errorcode
import json
import math


#
class DBSearch(object):

    def __init__(self, search_value, country, lang, page_num):
        self.search_value = search_value
        self.country = country
        self.lang = lang
        self.items_dict_search = {}
        self.item_type = ''
        self.page_num = page_num
        self.item_per_page = 20
        self.num_of_pages = 0
        self.offset = 0

    def pagination(self, all_results_len):
        self.num_of_pages = math.ceil(all_results_len / self.item_per_page)
        self.offset = (self.page_num - 1) * self.item_per_page

    def pagination_queries(self, q_mum):
        queries = {
            # search for item tybe by search_key in db
            'query_0': f"""SELECT item_type_en FROM main_schema.search_mapping WHERE 
                       MATCH(search_key_s) against('+\"{self.search_value}\"' IN BOOLEAN MODE) 
                       order by search_order ASC limit 1""",
            # search by keyword after get item tybe from first query
            'query_1': f"""SELECT  count(*) 
                       FROM main_schema.products_{self.country} WHERE item_type_en like '%{self.item_type}%' AND 
                       MATCH(title_en, title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE ) 
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None'
                       AND sold_out = 0 AND country like '%{self.country}%';""",
            # if item tybe found but search query not in the titles
            'query_2': f"""SELECT  count(*) 
                       FROM main_schema.products_{self.country} WHERE item_type_en like '%{self.item_type}%' 
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None' 
                       AND sold_out = 0 AND country like '%{self.country}%';""",
            # search in entire database if no results in search_mapping table
            'query_3': f"""SELECT  count(*) 
                       FROM main_schema.products_{self.country} WHERE 
                       MATCH(title_en, title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE )  
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None' 
                       AND sold_out = 0 AND country like '%{self.country}%';"""
        }
        return queries.get(q_mum)

    def search_query(self, q_mum):

        queries = {
            # search for item tybe by search_key in db
            'query_0': f"""SELECT item_type_en FROM main_schema.search_mapping WHERE 
                       MATCH(search_key_s) against('+\"{self.search_value}\"' IN BOOLEAN MODE) 
                       order by search_order ASC limit 1""",
            # search by keyword after get item tybe from first query
            'query_1': f"""SELECT  website_name, UIC, unique_product_code, title_{self.lang} as item_title, 
                       brand_{self.lang}, images_url, item_type_{self.lang}, sub_category_{self.lang}, 
                       item_upc, product_direct_link_{self.lang} as product_direct_link, 
                       rating, number_of_reviews, JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) as item_price 
                       FROM main_schema.products_{self.country} WHERE item_type_en = '{self.item_type}' AND 
                       MATCH(title_en, title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE ) 
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None' 
                       AND sold_out = 0 AND country = '{self.country}' LIMIT {self.offset}, {self.item_per_page};""",
            # if item tybe found but search query not in the titles
            'query_2': f"""SELECT  website_name, UIC, unique_product_code, title_{self.lang} as item_title, 
                       brand_{self.lang}, images_url, item_type_{self.lang}, sub_category_{self.lang}, 
                       item_upc, product_direct_link_{self.lang} as product_direct_link, 
                       rating, number_of_reviews, JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) as item_price 
                       FROM main_schema.products_{self.country} WHERE item_type_en = '{self.item_type}' 
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None' 
                       AND sold_out = 0 AND country = '{self.country}' LIMIT {self.offset}, {self.item_per_page};""",
            # search in entire database if no results in search_mapping table
            'query_3': f"""SELECT  website_name, UIC, unique_product_code, title_{self.lang} as item_title, 
                       brand_{self.lang}, images_url, item_type_{self.lang}, sub_category_{self.lang}, 
                       item_upc, product_direct_link_{self.lang} as product_direct_link, 
                       rating, number_of_reviews, JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) as item_price 
                       FROM main_schema.products_{self.country} WHERE 
                       MATCH(title_en, title_{self.lang}) against('+{self.search_value}' IN NATURAL LANGUAGE MODE ) 
                       AND JSON_EXTRACT(JSON_EXTRACT(price_data, '$.egp.*'), 
                       CONCAT('$[',JSON_LENGTH(JSON_EXTRACT(price_data, '$.egp.*'))-1,'].price')) != 'None' 
                       AND sold_out = 0 AND country = '{self.country}' LIMIT {self.offset}, {self.item_per_page};"""

        }

        return queries.get(q_mum)

    def db_connection(self):
        try:
            conn = mysql.connector.connect(user="admin", password="PTS-0000",
                                           host="129.159.205.97", port=3306, database="main_schema")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()
            cursor.execute(self.pagination_queries('query_0'))  # execute query
            result = cursor.fetchall()
            if result:
                self.item_type = result[0][0]
                query_to_execute = 'query_1'
                cursor.execute(self.pagination_queries('query_1'))
                result = cursor.fetchall()
                if not result or result[0][0] < 6:
                    query_to_execute = 'query_2'
                    cursor.execute(self.pagination_queries('query_2'))
                    result = cursor.fetchall()
            else:
                query_to_execute = 'query_3'
                cursor.execute(self.pagination_queries('query_3'))
                result = cursor.fetchall()
            self.pagination(result[0][0])
            # print(self.search_query(query_to_execute))
            # print(self.search_query(query_to_execute))
            cursor = conn.cursor(dictionary=True)
            print(self.search_query(query_to_execute))
            cursor.execute(self.search_query(query_to_execute))
            result = cursor.fetchall()
            # print('ttt' + str(result))

            # print(result)
            # if not result:
            #     cursor.execute(self.search_query('2'))
            #     result = cursor.fetchall()
            # items_dict_search = {}
            # for item in result:
            #     if item[0] not in items_dict_search:
            #         items_dict_search = {
            #             item[0]: {  # store
            #             }
            #         }
            #     item_dict_search = {
            #         item[2]: {  # item_uid
            #             'website_name': item[0],  #
            #             'item_uid': item[1],
            #             'unique_product_code': item[2],  #
            #             'item_title': item[3],
            #             'brand_en': item[4],  #
            #             'item_image': item[5].split('\n')[0],
            #             'item_type_en': item[6],  #
            #             'sub_category_en': item[7],  #
            #             'item_upc': item[8],  #
            #             'link_en': item[9],  #
            #             'item_url': item[10],
            #             'rating': item[11],  #
            #             'number_of_reviews': item[12],  #
            #             'item_price': item[13],
            #
            #         }
            #     }
            #     items_dict_search[item[0]].update(item_dict_search)
            self.items_dict_search = json.dumps(result)
            return [self.items_dict_search, self.num_of_pages]


# print(DBSearch('apple', 'eg', 'ar', 1).db_connection())
