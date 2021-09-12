import mysql.connector
from mysql.connector import errorcode
import json


class UploadDB:
    def __init__(self, json_data):
        self.json_items = json_data

    def db_connection(self):
        try:
            conn = mysql.connector.connect(user="admin", password="Api-0000",
                                           host="129.159.205.105", port=3306, database="main_schema")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with the user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cursor = conn.cursor()

    def extract_json(self):

        for item in self.json_items:
            print(item)
            pass
        pass
