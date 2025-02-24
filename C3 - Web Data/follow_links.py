import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = "http://py4e-data.dr-chuck.net/known_by_Amaia.html"
sample_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

position = 18
d_times = 7
times = 0

tags = soup('a')

first_element = url
lst = [first_element]
new_lst = [first_element]

for tag in tags:
   #print(tag.get('href', None))
   tag_str = str(tag.get('href',None))
   lst.append(tag_str)

for element in lst:
   while times <= d_times:
      new_lst.append(lst[position-1])
      position = position + 1
      print(position,times)
      times = times + 1
      print(new_lst[times])
      #print(lst[position])

print(new_lst)