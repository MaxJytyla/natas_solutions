from bs4 import BeautifulSoup
import requests
import urllib.parse
import base64
import concurrent.futures


def make(url, auth, my_params):
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    return res

def writeResponse(response, enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(BeautifulSoup(response.text, 'html.parser').prettify())

def decipher(encStr):
    return urllib.parse.unquote(encStr) #return base64.b64decode(urllib.parse.unquote(encStr)).hex()

def recipher(decStr):
    return urllib.parse.quote(base64.b64encode(bytes.fromhex(decStr)))


def urlQuery(url, auth, my_params):
    return decipher(make(url,auth,my_params).url[60:])

def numToCode(x):
    return [x,urlQuery(url, lvl_pass, {'query':'A'*x})]

def ntc(x):
    return [x,urlQuery(url, lvl_pass, {'query':'%'*x + "'from users;\#"})]

lvl_name = 'natas28'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
url = f'http://{lvl_name}.natas.labs.overthewire.org'
NUM_CODES=50
BLOCK_SIZE=16
OFFSET = 10

with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_CODES) as executor:
    codes = [x for x in executor.map(numToCode, list(range(NUM_CODES+1)))]

for x in codes:
    space_x = x[1][:OFFSET] + ' ' + ' '.join([x[1][i:i+(BLOCK_SIZE)] for i in range(OFFSET, len(x[1]), BLOCK_SIZE)])
    print(f'{x[0]:2}  -->    {len(x[1]):5}: {space_x}')
