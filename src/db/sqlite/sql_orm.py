import sqlite3
import json
from datetime import datetime

class SqliteObj():
    def __init__(self):
        self.sqlite_connection = sqlite3.connect('src\db\sqlite\sql.db', check_same_thread=False,
                            detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)
        self.cursor_obj = self.sqlite_connection.cursor()

    def create_table(self,table_name):
        try:
            table_list = self.cursor_obj.execute(
    f"""SELECT name FROM sqlite_master WHERE type='table'
    AND name='{table_name}'; """).fetchall()
            if table_list == []:
                print('Table not found!')
                # Creating table
                table = f""" CREATE TABLE {table_name} (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            UserID INT,
                            CreateTime TIMESTAMP NOT NULL,
                            ExtractedText VARCHAR(255),
                            FileDirectory VARCHAR(255) NOT NULL
                        ); """
                self.cursor_obj.execute(table)
            else:
                print('Table found!')
        except Exception as e:
            pass

    def insert(self,data):
        # create query to insert the data
        query = """INSERT INTO TEST (UserID,CreateTime,ExtractedText,FileDirectory) VALUES (?, ?, ?, ?);"""
        current_time = datetime.now()
        user_id = data['userid']
        file_dir = f'\\src\\db\\received_files\\{user_id}\\' + data['filename']
        self.cursor_obj.execute(query, (user_id,current_time,data['res_text'],file_dir))

    def read(self):
        query = '''SELECT * FROM test WHERE userid = 12 '''
        self.cursor_obj.execute(query)
        output = self.cursor_obj.fetchmany(20)
        for row in output:
            print(row)
        return output

    def search(self,search_query):
        query = f'''SELECT * FROM test WHERE userid = 12 AND ExtractedText LIKE "%{search_query}%" '''
        self.cursor_obj.execute(query)
        output = self.cursor_obj.fetchall()
        for row in output:
            print(row)
        return output

    def modify_data(self, update_txt, data_id):
        query = f'''UPDATE test SET ExtractedText = "{update_txt}" WHERE id = {data_id}'''
        self.cursor_obj.execute(query)
        self.sqlite_connection.commit()
        print('done')

