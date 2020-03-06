from django.contrib import admin

# Register your models here.
from blog.models import Post
from blog.models import PhotoPost
from blog.models import Category
from blog.models import Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug', 'category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'published')


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(PhotoPost)
