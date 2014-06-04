from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# Create your views here.

from .models import Posts

def list_posts(request):
    posts = Posts.objects.all()
    template = loader.get_template('list.html')
    context = RequestContext(request, {"A":1, "posts" : posts })
    return HttpResponse( template.render(context))
