from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=60)
    body=models.TextField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def get_absolute_url(self):
        return "/blog/posts/%i/true" % self.id

    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    body=models.TextField()
    author=models.CharField(max_length=60)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    post=models.ForeignKey(Post)
    def body_first60(self):
        return self.body[:60]
    def __unicode__(self):
        return self.body


