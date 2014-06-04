from django.conf.urls import patterns, include, url

urlpatterns = patterns('simpleboard.views',
    url(r'^list/$', 'list_posts',name='list_posts'),
    url(r'^post/(?P<post_id>\d+)$', 'view_post',name='view_post'),
    url(r'^delete/(?P<post_id>\d+)$', 'delete_post',name='delete_post'),
    url(r'^write/$', 'write_post',name='write_post'),
)
