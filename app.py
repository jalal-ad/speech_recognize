from fastapi import File, UploadFile, FastAPI
from src.speech_recognizer import AudioRecognize
from src.db.sqlite import Sqlite
import shutil
from time import sleep

import pathlib
file_path = str( pathlib.Path(__file__).absolute().parent )

Sqlite.sqlite.create_table('test')

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
        data={
            'userid': user_id,
            'res_text': result_text,
            'filename':file.filename
        }
        Sqlite.sqlite.insert(data)
        
        Sqlite.sqlite.sqlite_connection.commit()
        Sqlite.sqlite.cursor_obj.close()
        Sqlite.sqlite.sqlite_connection.close()

    return {"message": f"Successfully uploaded {file.filename}, text: {result_text}"}