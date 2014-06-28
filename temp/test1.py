#!/usr/bin/python
import urllib
import re
import StringIO
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#soup = BeautifulSoup(html_doc)
#print soup.prettify()

last = BeautifulSoup(urllib.urlopen('https://play.google.com/store/apps/details?id=jp.naver.line.android'))
reviews = last.find_all("div", "single-review")

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


a1=last.find("div", "reviews-heading")
#print a1.prettify()