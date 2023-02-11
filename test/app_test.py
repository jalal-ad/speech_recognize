import requests

# url = 'http://127.0.0.1:8000/upload'
# file = {'file': open('test/speech1.mp3', 'rb')}
# resp = requests.post(url=url, files=file, params={'username':'admin','password':'Admin@123'}) 
# print(resp.json())

url = 'http://127.0.0.1:8000/history'
resp = requests.get(url=url, params={'username':'admin','password':'Admin@123'}) 
print(resp.json())