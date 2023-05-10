from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        
        
lvl_name = 'natas5'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD')
my_cookies = {'loggedin':'1'}


res, soup = make()
writeResponse()

'''
Lesson: Cookies are recieved from the end-client and can be easily modified by the client.
Either encrypt them well so that meaningful changes cannot be made, or do not rely on them
for important actions.

Username: natas6
Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR
 
'''