#!/usr/bin/python

import mechanize
import urllib
from bs4 import BeautifulSoup
import json
import time

browser = mechanize.Browser()
pageNum=0;

while 1:
    param = { 'reviewType': '0', 'pageNum': pageNum, 'id': 'jp.naver.line.android', 'reviewSortOrder': '0', 'xhr': '1' }
    data = urllib.urlencode(param)
    browser.set_handle_robots(False)
    resp = browser.open('https://play.google.com/store/getreviews', data)
    content = json.loads(resp.read()[5:])

    if len(content) != 0 and content[0][0] != 'ger' :
    # data3 = json.loads(data2)
    # print type(data3) , len(data3) , type(data3[0]) , len(data3[0])
    # print data2[0][0]
    # print data2[0][1]
    # print data2[0][2].encode("utf8")
    # print data2[0][3]
        bs5 = BeautifulSoup(content[0][2].encode("utf8"))
        reviews = bs5.find_all("div", "single-review")
        for review in reviews:
            cur_date = review.find("span", "review-date")
            body = review.find("div", "review-body")
            
            review_date =  cur_date.string
            review_title = body.contents[1].string
            review_content = body.contents[2].string
            
            print "Date :" , review_date
            print "Title :" , review_title
            print "Content :" , review_content
            print "\n"
    else:
        print "data not exists"
        break
    if pageNum > 3:
        break
    time.sleep(3)
    pageNum+=1
    


# https://play.google.com/store/apps/details?id=jp.naver.line.android 