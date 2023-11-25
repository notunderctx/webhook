import requests

url = "http://127.0.0.1:5000/hook"

data = {"sender": "sumguy@gmail.com", "message": "......s"}

requests.post(url=url, data=data)
