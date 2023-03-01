from bs4 import BeautifulSoup
import requests
import re
def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())

lvl_name = 'natas11'
url = f'http://{lvl_name}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg')
my_cookies = {'data':'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbXB7KCstLmkz'}#'R0EWBhwYAgQXTUsMFwpRVVAcAU0eT0cMFAwdCQtMHllHTUtYMSAhfB4e'} #This is where the magic happens.
my_params = {"bgcolor":"87CEEB"}
res, soup = make()
writeResponse()
print(re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0])

'''
Took me a bit to remember how to do this one.

This one is made FAR easier by a home PHP site to test on. By doing XOR encryption on a ciphertext (recieved from the cookies)
with the key as the plaintext, you recieve the actual key. (In this case the key was KNHL, though it changes periodically).

Username: natas12
Password: YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

'''
