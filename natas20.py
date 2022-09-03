from bs4 import BeautifulSoup
import requests

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)
    
def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())
        

url = 'http://natas20.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas20','eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
my_cookies = {"PHPSESSID":'bac'}
my_params = {"name":"what", "password":"whatever", "debug":"true"}

res, soup = make()
writeResponse()
'''
This one was fucking weird, I solved it by running the above script in the py CLI
Because I saw that everything in the Session file is read into the $_SESSION array,
but only the $_SESSION["name"] key/value pair is WRITTEN into the file. in the form

name {your submitted name here}

So, by setting my parameters as $_REQUEST["name"] => "someName\nadmin 1" to write that into
the file, then making another request to read all that OUT of the session file, I got admin set
to 1.

Username: natas21
Password: IFekPyrQXftziDEsUr3x21sYuahypdgJ 
'''
