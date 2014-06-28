from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from .models import Posts
from django.db.models import F
from django.forms import ModelForm


import mechanize
import urllib
from bs4 import BeautifulSoup
import json
import time



# Create your views here.
def list_posts(request):
    posts = Posts.objects.order_by("-id").all()
    template = loader.get_template('list.html')
    


    Mainlist= [];
    Sublist= [];
    browser = mechanize.Browser()
    pageNum=0;
    review_date=0;
    review_title=0;
    review_content=0;

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

                Sublist.append(review_date);
                Sublist.append(review_title);
                Sublist.append(review_content);

                Mainlist.append(Sublist);
                Sublist= [];

        else:
            print "data not exists"
            break
        if pageNum > 1:
            break
        #time.sleep(3)
        pageNum+=1

    print type(posts)
    context = RequestContext(request, {"A":2, "posts" : posts, "Mainlist" : Mainlist })
    return HttpResponse( template.render(context))

def view_post(request, post_id=None):
    Posts.objects.filter(id=post_id).update(read_counter=F("read_counter") + 1 )
    post = Posts.objects.get(id=post_id)
    template = loader.get_template('view.html')
    context = RequestContext(request, {"A":1, "post" : post })
    return HttpResponse( template.render(context))

def delete_post(request, post_id=None):
    post = Posts.objects.get(id=post_id)
    post.delete()
    return redirect("/list")

class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['writer', 'subject', 'content']

def write_post(request):
    # if GET , print form
    if request.method == "GET":
        form = PostForm()
        template = loader.get_template('form.html')
        context = RequestContext(request, {"form" : form })
        return HttpResponse( template.render(context))
    # if POST, save form => return to post page
    form = PostForm(request.POST)
    new_post = form.save()
    print "new post page id ", new_post.id
    return redirect("/post/%s" % new_post.id)
    #return redirect("/list/")
