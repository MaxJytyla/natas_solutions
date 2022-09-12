from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        

url = 'http://natas0.natas.labs.overthewire.org'  
lvl_pass = requests.auth.HTTPBasicAuth('natas0','natas0')

res, soup = make()
writeResponse()

'''
PW in raw markup comment

Username: natas1
Password: g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
'''