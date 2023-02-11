from fastapi import File, UploadFile, FastAPI
app = FastAPI()

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(file.filename, 'wb') as f:
            print('message: file received')
    except Exception as e:
        return {"message": f"There was an error uploading the file {e}"}
    finally:
        file.file.close()
        
    return {"message": f"Successfully uploaded {file.filename}"}