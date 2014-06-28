#!/usr/bin/python
import requests
import logging

# These two lines enable debugging at httplib level (requests->urllib3->httplib)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
import httplib
#httplib.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
# logging.basicConfig() 
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = False

#requests.get('https://httpbin.org/headers')
# r = requests.get('https://play.google.com/store/apps/details?id=jp.naver.line.android')

# r.cookies['cookies']

#url = 'http://example.com/some/cookie/setting/url'
url = 'https://play.google.com/store/apps/details?id=jp.naver.line.android'
r = requests.get(url)

print r.cookies['PLAY_PREFS']
print r.cookies['NID']


# url = 'http://httpbin.org/cookies'
cookies = dict(PLAY_PREFS=r.cookies['PLAY_PREFS'], NID=r.cookies['NID'])

r = requests.get(url, cookies=cookies)
print r.text



s = requests.Session()
r = s.get("https://play.google.com/store/apps/details?id=jp.naver.line.android")
r.text