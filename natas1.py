from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        
lvl_name = 'natas1'
url = f'http://{lvl_name}.natas.labs.overthewire.org'  
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','g9D9cREhslqBKtcA2uocGHPfMZVzeFK6')

res, soup = make()
writeResponse()

'''
PW in raw markup comment

Username: natas2
Password: h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 
'''