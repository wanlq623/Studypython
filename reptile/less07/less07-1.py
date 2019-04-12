import requests

url = 'https://www.shanbay.com/api/v1/vocabtest/category/'
res = requests.get(url)
web_json = res.json()
print(web_json)