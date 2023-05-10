from bs4 import BeautifulSoup
import requests

def make():
    res = requests.post(url=url,auth=lvl_pass, data=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
lvl_name = 'natas8'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB')
my_params = {'secret':'oubWYf2kBq', 'submit':'Submit'}

res, soup = make()
writeResponse()

'''
Not sure how to do this in Python actually. I solved this by running the Apache PHP server I have at home,
and computing the encodedSecret found in the source file as follows

$str = base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
echo($str)

Username: natas9
Password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
 
'''