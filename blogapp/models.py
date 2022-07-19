from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
import os
from django.urls import reverse



# Create your models here.
class Blog_Post(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE)
    created_on = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    Commenter = models.CharField(max_length= 50)
    body = models.TextField()
    post = models.ForeignKey(Blog_Post, on_delete= models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body
    
    
def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    bio = models.CharField(max_length=150, blank=True)
    
    profile_pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)
    
    ministers  = 'ministers'
    members = 'members'
    user_types = [
        (ministers, 'ministers'),
        (members, 'members'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types, default=members)
    
    def __str__(self):
        return self.user.username
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')
    
class AboutUs(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    body = models.TextField(max_length=500)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
class UpcomingEvents(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    body = models.TextField(max_length = 500)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
    