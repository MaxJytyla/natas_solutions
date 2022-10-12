import requests as r
import base64 as b64
import concurrent.futures
from urllib.parse import unquote as uq
lvl_name = 'natas28'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
q = 'x'
lvl_pass = r.auth.HTTPBasicAuth(f'{lvl_name}','skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')




def srch(num):
    query = 'x'*num
    return  [num, uq(r.post(url=url, auth=lvl_pass, params={'query':query}).url[60:])]

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    results = list(executor.map(srch, list(range(50))))


