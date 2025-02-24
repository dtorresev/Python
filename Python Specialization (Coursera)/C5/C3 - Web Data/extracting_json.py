import urllib.request
import json

lst  = []
suma = 0
c = 0

url = "https://py4e-data.dr-chuck.net/comments_2047989.json"
sample_url = "https://py4e-data.dr-chuck.net/comments_42.json"

uh = urllib.request.urlopen(url)
data = uh.read()

info = json.loads(data)
counts = []

if 'comments' in info:
    comments = info['comments']
    print('User count:', len(comments))
    
    # Iterate over the comments list to print user names
    for item in comments:
        print('Name:', item['name'])
        print('Count:',item['count'])
        counts.append(int(item['count']))

print('Counts:', sum(counts))

