from django.contrib import admin
from blog.models import Post
app_name = 'blog'
# Register your models here.
admin.site.register(Post)