from bs4 import BeautifulSoup
import requests
import re

lvl = '8'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_params = {'secret':'oubWYf2kBq', 'submit':'Submit'}

soup = BeautifulSoup(requests.post(url=url,auth=lvl_pass, data=my_params).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)

'''
Not sure how to do this in Python actually. I solved this by running the Apache PHP server I have at home,
and computing the encodedSecret found in the source file as follows

$str = base64_decode(strrev(hex2bin("3d3d516343746d4d6d6c315669563362")));
echo($str)

Username: natas9
Password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd

'''
