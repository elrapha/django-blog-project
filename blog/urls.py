from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'home'),
    url(r'^posts/$', 'post_list'),
    url(r'^posts/(?P<ID>\d+)/((?P<showComments>.*)/)?$', 'post_detail'),
    #url(r'^posts/(\d+)(/\w)*$', 'blog.views.post_detail'),
    url(r'^posts/search/(\w+)/','post_search'),
    ## add your url here
)
