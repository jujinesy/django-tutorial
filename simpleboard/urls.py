from django.conf.urls import patterns, include, url

urlpatterns = patterns('simpleboard.views',
    url(r'^list/$', 'list_posts',name='list_posts'),
)
