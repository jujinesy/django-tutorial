#!/usr/bin/python

import requests


# r = requests.get('https://github.com/timeline.json')
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get("http://httpbin.org/get", params=payload)


# print(r.url)

# r.content



# r = requests.get('http://httpbin.org/get', stream=True)
# r.raw
# r.raw.read(10)


r = requests.get('https://github.com/timeline.json')
print r.json()