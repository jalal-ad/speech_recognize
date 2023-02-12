from fastapi import File, UploadFile, FastAPI
from src.speech_recognizer import AudioRecognize
from src.db.sqlite import Sqlite
import shutil
from time import sleep

import pathlib
file_path = str( pathlib.Path(__file__).absolute().parent )

Sqlite.sqlite.create_table('test')
# Sqlite.sqlite.cursor_obj.close()
# Sqlite.sqlite.sqlite_connection.close()

user_id = 12
app = FastAPI()

# upload audio file with mp3 format & save recognized text on db
@app.post("/upload")
def upload(username: str, password: str,file: UploadFile = File(...)):
    if username=='admin' and password=='Admin@123':
        try:
            # get text from audio file
            result_text = AudioRecognize.recognizer(file).run('speech1')

            # insert data into db
            data={
                'userid': user_id,
                'res_text': result_text,
                'filename':file.filename
            }
            Sqlite.sqlite.insert(data)
            Sqlite.sqlite.sqlite_connection.commit()

        except Exception as e:
            return {"message": f"There was an error uploading the file: {e}"}
        finally:
            file.file.close()
            sleep(1)

            # move uploaded file to user directory
            dest_dir = file_path + f'\\src\\db\\received_files\\{user_id}\\' + file.filename
            shutil.move(file.filename, dest_dir)

        return {"message": f"Successfully uploaded {file.filename}, text: {result_text}"}

# see last 20 user request history
@app.get("/history")
def get_history(username: str, password: str):
    if username=='admin' and password=='Admin@123':
        history = Sqlite.sqlite.read()
        return history

# search in text
@app.get("/history/search")
def get_history(username: str, password: str, search_pattern: str):
    if username=='admin' and password=='Admin@123':
        history = Sqlite.sqlite.search(search_pattern)
        return history