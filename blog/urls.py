from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'home'),
    url(r'^posts/$', 'post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$','post_detail'),
    url(r'^posts/search/((?P<term>\w+)/)?$','post_search'),
    url(r'^comments/(?P<comID>\d+)/edit/','edit_comment'),
    ## add your url here
)
