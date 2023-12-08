from django.contrib import admin
from .models import User, BlogPost

# Register your models here.
admin.site.register(User)
admin.site.register(BlogPost)
