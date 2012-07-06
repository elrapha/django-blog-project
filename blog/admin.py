from django.contrib import admin
from blog.models import Post
from blog.models import Comment


class CommentInline(admin.TabularInline):
    model=Comment
    
class PostAdmin(admin.ModelAdmin):
    list_display=('title','created','updated')
    search_fields=('title','body')
    list_filter=('created',)
    inlines=[CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display=('author','body_first60','updated')
    list_filter=('created','author')
    def body_first60(self,empty):
        return self.body[:60]


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)


