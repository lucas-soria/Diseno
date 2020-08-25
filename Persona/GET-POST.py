from requests import get
from requests import post
from requests import delete
from requests import put
import json


url = 'http://localhost:5000/api/Welcome'
r = get(url)
print(r.content.decode())


url = 'http://localhost:5000/api/Persona'
payload = {
    'id': 42421815,
    'name': 'Franco',
    'surname': 'Santander',
    'age': 20,
    }
r = post(url, data=json.dumps(payload))
payload = {
    'id': 42670460,
    'name': 'Lucas',
    'surname': 'Soria',
    'age': 20,
    }
r = post(url, data=json.dumps(payload))
payload = {
    'id': 42168800,
    'name': 'Valentina',
    'surname': 'Scalco',
    'age': 20,
    }
r = post(url, data=json.dumps(payload))
payload = {
    'id': 42494094,
    'name': 'Philipp',
    'surname': 'Von Kesselstatt',
    'age': 20,
    }
r = post(url, data=json.dumps(payload))
payload = {
    'id': 651654654,
    'name': 'akjsdhakshd',
    'surname': 'lkajshdkasjda',
    'age': 600,
    }
r = post(url, data=json.dumps(payload))


r = get(url)
print(r.content.decode())


payload = {
    'id': 42670460,
    'name': 'Lucas Damian',
    'surname': 'Soria Gava',
    'age': 20
    }
r = put(url, data=json.dumps(payload))


payload = {'id': 42494094}
r = delete(url, data=json.dumps(payload))


"""
python migrate.py db init
python migrate.py db migrate
python migrate.py db upgrade
python run.py
"""
