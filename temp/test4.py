#!/usr/bin/python

import requests

url = 'https://play.google.com/store/apps/details?id=jp.naver.line.android'
s = requests.Session()
s.get(url)