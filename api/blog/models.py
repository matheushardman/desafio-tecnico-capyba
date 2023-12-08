from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_image_profile(instance, filename):
   return f"{instance.username}-{filename}"

# Classe usuário
class User(AbstractUser):
    email = models.EmailField(unique=True, blank = False)
    name = models.CharField(max_length=100, blank = False)
    profile_photo = models.ImageField(upload_to=upload_image_profile, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

# Classe Blog

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=True)