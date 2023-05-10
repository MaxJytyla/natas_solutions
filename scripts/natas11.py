from bs4 import BeautifulSoup
import requests
import re

lvl = '11'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_cookies = {'data':'MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbXB7KCstLmkz'}
my_params = {"bgcolor":"87CEEB"}
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass, cookies=my_cookies, params=my_params).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''
Took me a bit to remember how to do this one.

This one is made FAR easier by a home PHP site to test on. By doing XOR encryption on a ciphertext (recieved from the cookies)
with the key as the plaintext, you recieve the actual key. (In this case the key was KNHL, though it changes periodically).

Username: natas12
Password: YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG

'''
