import urllib.request
import xml.etree.ElementTree as ET

#sample_url = "https://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_2047988.xml"
uh = urllib.request.urlopen(url)
data = uh.read()
#data = '''<comments> <comment> <name>Laurie</name> <count>97</count> </comment> </comments>'''

print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)
counts = tree.findall('comments/comment')
nums = []

print("User count", len(counts))

for item in counts:
    print("Count", item.find('count').text)
    nums.append(int(item.find('count').text))

print("Count: ", len(nums))
print("Sum: ", sum(nums))

