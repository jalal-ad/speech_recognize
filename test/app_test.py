import requests

# url = 'http://127.0.0.1:8000/upload'
# file = {'file': open('test/speech1.mp3', 'rb')}
# resp = requests.post(url=url, files=file, params={'username':'admin','password':'Admin@123'}) 
# print(resp.json())

# url = 'http://127.0.0.1:8000/history'
# resp = requests.get(url=url, params={'username':'admin','password':'Admin@123'}) 
# print(resp.json())

# url = 'http://127.0.0.1:8000/history/search'
# resp = requests.get(url=url, params={'username':'admin','password':'Admin@123','query':'م'}) 
# print(resp.json())

url = 'http://127.0.0.1:8000/update'
resp = requests.put(url=url, params={'username':'admin','password':'Admin@123','updtxt':'سلام','dataid':3}) 
print(resp.json())

url = 'http://127.0.0.1:8000/delete'
resp = requests.delete(url=url, params={'username':'admin','password':'Admin@123','dataid':4}) 
print(resp.json())