from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import redirect
from .models import Posts
from django.db.models import F
from django.forms import ModelForm

# Create your views here.
def list_posts(request):
    posts = Posts.objects.order_by("-id").all()
    template = loader.get_template('list.html')
    context = RequestContext(request, {"A":2, "posts" : posts })
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
