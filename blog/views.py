# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

#from django.template import Context, loader
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 


def post_list(request):
    list_of_post= Post.objects.all()
    
    #return HttpResponse('This should be a list of posts!')
    return render_to_response('post_list.html',locals())

def post_detail(request, ID, showComments):
    POST=Post.objects.get(id=ID)
    title=POST.title
    body=POST.body
    created=POST.created
    updated=POST.updated
    comments=''
    if showComments!=None:
        comments=POST.comment_set.all()
        
    return render_to_response('post_details.html',locals())
    
def post_search(request, term):
    keyword=term
    list_of_post = Post.objects.filter(body__icontains=term)
    return render_to_response('post_search.html',locals())

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 









