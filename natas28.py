from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())

lvl_name = 'natas28'
url = f'http://{lvl_name}.natas.labs.overthewire.org'

lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
my_cookies = {}

my_params = {'query':'%'}

#res, soup = make()
#writeResponse()
