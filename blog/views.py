
# Create your views here.

"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

#from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import Post, Comment 
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


def post_list(request):
    list_of_post= Post.objects.all()
    
    #return HttpResponse('This should be a list of posts!')
    return render_to_response('post_list.html',locals())

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		exclude=['post']
		
@csrf_exempt
def post_detail(request, id, showComments):
    POST=Post.objects.get(id=id)
    if request.method == 'POST':
        comment = Comment(post=POST)
        form = CommentForm(request.POST,instance=comment)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()

    
    title=POST.title
    body=POST.body
    created=POST.created
    updated=POST.updated
    comments=''
    if showComments!=None:
        comments=POST.comment_set.all()

    return render_to_response('post_details.html',locals())

@csrf_exempt
def edit_comment(request,comID):
    comment=Comment.objects.get(id=comID)
    Related_Post=comment.post
    POST=Post.objects.get(pk=Related_Post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=Comment.objects.get(id=comID))
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(POST.get_absolute_url())
    else:
        form = CommentForm(instance=Comment.objects.get(id=comID))
        
    return render_to_response('edit_comment.html',locals())

def post_search(request, term):
    keyword=term
    list_of_post = Post.objects.filter(body__icontains=term)
    return render_to_response('post_search.html',locals())

def home(request):
    #print 'it works'
    #return HttpResponse('hello world. Ete zene?')
    return render_to_response('post_home.html','') 









