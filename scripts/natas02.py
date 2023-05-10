from bs4 import BeautifulSoup
import re
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())


lvl_name = 'natas2'
url = f'http://{lvl_name}.natas.labs.overthewire.org/files/users.txt'  #New directory target
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7')

res, soup = make()
writeResponse()
print(re.search(r"^natas3:.*$", soup.text,re.MULTILINE)[0][-32:])
'''
Simple directory traversal lesson.

Username: natas3
Password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q

'''
