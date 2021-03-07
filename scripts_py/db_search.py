import mysql.connector
from mysql.connector import errorcode
import json


def db_connection(search_value):
    try:
        conn = mysql.connector.connect(user="root", password="",
                                       host="localhost", port=3306, database="test")
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
            "SELECT Website_Name, Title_EN, Title_AR, Unique_Product_Code, link_en, Price_eg, Images_URL, Brand_EN, "
            "Brand_AR, Item_Type_EN, Item_Type_AR, UIC, link_ar, Item_UPC, Product_Direct_Link_EN,"
            "Product_Direct_Link_AR FROM Products WHERE MATCH(Item_Type_EN, Title_EN) "
            "against('%{}%' IN NATURAL LANGUAGE MODE) AND Price_eg IS NOT NULL "
            "AND Country like '%EG%' LIMIT 30".format(search_value))
        result = cursor.fetchall()
        items_dict_search = {}
        for item in result:
            if item[0] not in items_dict_search:
                items_dict_search = {
                    item[0]: {
                    }
                }
            item_dict_search = {
                item[3]: {
                    "item_title": item[1],
                    "item_title_AR": item[2],
                    "item_image": item[6].split("\n")[0],
                    "item_price": item[5],
                    "item_url": item[14],
                    "item_url_ar": item[15],
                    "item_uid": item[3]
                }
            }
            items_dict_search[item[0]].update(item_dict_search)
        return json.dumps([items_dict_search])


