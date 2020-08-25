# from requests import get
from requests import post
import json


url = 'http://localhost:5000/api/Category'
payload = {'name': 'Valentina', }
r = post(url, data=json.dumps(payload))
print(r.json())
url = 'http://localhost:5000/api/Comment'
payload = {'category_id': '2', 'comment': 'Valentina la "PEOR"'}
r = post(url, data=json.dumps(payload))
print(r.json())
# r = get(url)
# print(r.text)
