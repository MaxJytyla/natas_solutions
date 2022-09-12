from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        
lvl_name = 'natas3'
url = f'http://{lvl_name}.natas.labs.overthewire.org/s3cr3t/users.txt'  #ALSO New directory target
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q')

res, soup = make()
writeResponse()

'''
Directory name located in robots.txt

Username: natas4
Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
 
'''