import sqlite3
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

