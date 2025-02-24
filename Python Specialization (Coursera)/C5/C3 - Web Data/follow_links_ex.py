import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


test_url = "http://py4e-data.dr-chuck.net/known_by_Amaia.html"
sample_url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

desired_element = 18
desired_tag = None
current_count = 0
count = 7

def parse_html(url):
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, "html.parser")
   tags = soup('a')
   return tags

while current_count <= count:
    print(test_url)
    tags  = parse_html(test_url)
    desired_tag = tags[desired_element-1]
    tag_str = str(desired_tag.get('href',None))
    current_count = current_count + 1
    test_url = tag_str
