from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, headers=my_headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        
lvl_name = 'natas4'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm')
my_headers = {'Referer': 'http://natas5.natas.labs.overthewire.org/'}


res, soup = make()
writeResponse()

'''
Lesson about HTTP request headers.

Username: natas5
Password: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD
 
'''