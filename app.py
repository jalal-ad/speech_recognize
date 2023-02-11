from fastapi import File, UploadFile, FastAPI
from src.speech_recognizer import AudioRecognize
import shutil

import pathlib
file_path = str( pathlib.Path(__file__).absolute().parent )

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

        # move uploaded file to user directory
        dest_dir = file_path + f'\\src\\db\\received_files\\{user_id}\\' + file.filename
        shutil.move(file.filename, dest_dir)
        
    return {"message": f"Successfully uploaded {file.filename}, text: {result_text}"}