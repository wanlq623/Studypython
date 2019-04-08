import requests

#res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

print(res.status_code)
#print(res.text)

with open('rescon.mp3','wb') as rescon:
    rescon.write(res.content)