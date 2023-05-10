from bs4 import BeautifulSoup
import requests

lvl = '0'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass).text, 'html.parser')
pw = soup.find("div",id="content").contents[1][-33:-1]


open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

'''
PW in raw markup comment

Username: natas1
Password: g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
'''
