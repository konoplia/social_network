from django.contrib import admin
from blog.models import BlogPost, Reaction
# # Register your models here.

admin.site.register(BlogPost)
admin.site.register(Reaction)
