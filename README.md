## Install dependencies

1. create venv with `python -m venv .venv` 
2. Enable your `venv`:
   * Linux and Mac users: `./.venv/bin/activate`
   * Windows users: `.\.venv\Scripts\activate`
3. in cmd run `pip install -r requirements.txt` (for windows users) 

## run app ##
1. build image `docker-compose build` 
2. run container `docker-compose up -d` 
3. get shell `docker exec -it {image_name} /bin/bash` 