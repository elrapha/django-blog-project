
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
from django.http import HttpResponseRedirect,HttpResponseForbidden

from reg.views import LoginForm

def post_list(request):
    logged_in =request.user.is_authenticated() # get login status
    list_of_post= Post.objects.all() # get all posts
    current_user=str(request.user) # get current user's name
    #return HttpResponse('This should be a list of posts!')
    return render_to_response('blog/post_list.html',locals()) #return

class CommentForm(ModelForm): # create a class that mimics the Comment class in models.py
    class Meta:
        model=Comment # make class of the same model as Comment in models.py
        exclude=['post','author'] # remove post and author fields from the form
		
@csrf_exempt
def post_detail(request, id, showComments):
    logged_in =request.user.is_authenticated()# get login status
    trueval="true"
    if request.user.is_authenticated(): #if user is authenticated
        P=Post.objects.get(id=id) # get post by id
        current_user=str(request.user) # get username as string
        if request.method == 'POST': # if user clicks submit button do...
            comment = Comment(post=P,author=current_user)# create instance of Comment with post and author attributes initialized
            form = CommentForm(request.POST,instance=comment)# get form field inputs
            if form.is_valid():#if form is valid
                form.save()# save in database
            return HttpResponseRedirect(request.path)
        else:
            form = CommentForm() # instance of empty form

        
        title=P.title
        body=P.body
        created=P.created
        updated=P.updated
        comments=''
        if showComments=="true":
            comments=P.comment_set.all()# get all comments associated with post P

        
        return render_to_response('blog/post_details.html',locals())
    else:
        return HttpResponseRedirect('/reg/login/')
        
@csrf_exempt
def edit_comment(request,comID):
    logged_in =request.user.is_authenticated() # get login status
    current_user=request.user #get current user
    comment=Comment.objects.get(id=comID) # get comment by id
    Related_Post=comment.post # get the related post of the comment
    P=Post.objects.get(pk=Related_Post.id)# get post 
    if request.method == 'POST': # if user clicks submit
        if str(current_user) == comment.author:
            form = CommentForm(request.POST,instance=Comment.objects.get(id=comID))
            if form.is_valid():
                form.save() # save in database
            return HttpResponseRedirect(P.get_absolute_url())
        else:
            return HttpResponseForbidden('Sorry. You are not allowed to edit this comment')
    else:
        form = CommentForm(instance=Comment.objects.get(id=comID))
        
    return render_to_response('blog/edit_comment.html',locals())


def post_search(request, term):
    logged_in =request.user.is_authenticated()# get login status
    current_user=str(request.user) # get current user
    if request.user.is_authenticated():
        keyword=term
        list_of_post = Post.objects.filter(body__icontains=term)# check if body of bost contains search term
        return render_to_response('blog/post_search.html',locals())
    else:
        return HttpResponseRedirect('/reg/login/')
def home(request):
    current_user=str(request.user)# get current user
    logged_in =request.user.is_authenticated()# get login status
    
    return render_to_response('blog/post_home.html',locals()) 









