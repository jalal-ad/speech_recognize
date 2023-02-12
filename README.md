# speech_recognize
speech recognition with vox &amp; fast-api

## Install dependencies

1. Create venv with `python -m venv .venv` 
2. Enable your `venv`: 
   * Linux and Mac users: `./.venv/bin/activate` 
   * Windows users: `.\.venv\Scripts\activate` 
3. Run `pip install -r requirements.txt` 
4. unzip model file: \src\speech_recognizer\model.rar

## run app ##
1. Build image `docker-compose build` 
2. Run container `docker-compose up -d` 
3. Get shell `docker exec -it {image_name} /bin/bash` 