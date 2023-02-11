from fastapi import File, UploadFile, FastAPI
from src.speech_recognizer import AudioRecognize
import shutil
import sqlite3
from datetime import datetime
from time import sleep

import pathlib
file_path = str( pathlib.Path(__file__).absolute().parent )

sqlite_connection = sqlite3.connect(file_path+ '\src\db\sqlite\sql.db', check_same_thread=False,
                            detect_types=sqlite3.PARSE_DECLTYPES |
                             sqlite3.PARSE_COLNAMES)
cursor_obj = sqlite_connection.cursor()

table_list = cursor_obj.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='TEST'; """).fetchall()
 
if table_list == []:
    print('Table not found!')
    # Creating table
    table = """ CREATE TABLE TEST (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                UserID INT,
                CreateTime TIMESTAMP NOT NULL,
                ExtractedText VARCHAR(255),
                FileDirectory VARCHAR(255) NOT NULL
            ); """
    cursor_obj.execute(table)
else:
    print('Table found!')

# query = 'SQL query;'
# cursor.execute(query)
# result = cursor.fetchall()
# print('SQLite Version is {}'.format(result))

app = FastAPI()

user_id = 12
@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        result_text = AudioRecognize.recognizer(file).run('speech1')

    except Exception as e:
        return {"message": f"There was an error uploading the file: {e}"}
    finally:
        file.file.close()
        sleep(1)

        # move uploaded file to user directory
        dest_dir = file_path + f'\\src\\db\\received_files\\{user_id}\\' + file.filename
        shutil.move(file.filename, dest_dir)

        # insert data into db
        # create query to insert the data
        query = """INSERT INTO TEST (UserID,CreateTime,ExtractedText,FileDirectory) VALUES (?, ?, ?, ?);"""
        current_time = datetime.now()
        file_dir = f'\\src\\db\\received_files\\{user_id}\\' + file.filename
        cursor_obj.execute(query, (12,current_time,result_text,file_dir))
        
        sqlite_connection.commit()
        cursor_obj.close()
        sqlite_connection.close()

    return {"message": f"Successfully uploaded {file.filename}, text: {result_text}"}