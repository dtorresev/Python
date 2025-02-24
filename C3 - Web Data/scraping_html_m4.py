from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst  = []
suma = 0
c = 0

url = "http://py4e-data.dr-chuck.net/comments_2047986.html"
sample_url = "https://py4e-data.dr-chuck.net/comments_42.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('tr')
for tag in tags:
   # Look at the parts of a tag
   print ('TAG:',tag)
   contents = tag.contents[0]
   print (contents)
   cts = str(contents)
   print(cts.strip("<td>,</td>"))
   string = str(tag)
   num = re.findall('[0-9]+', string)
   for i in num:
      print(num)
      if int(i) > 0:
         lst.append(i)
   
for n in lst:
   suma = suma + int(n)
   c = c + 1 
   
print(suma)
print(c)
