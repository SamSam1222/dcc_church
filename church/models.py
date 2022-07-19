from email.mime import image
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os

class Standard(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)

class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
    image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500,blank=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)
        
def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name, ext)
    return os.path.join(upload_to, filename)       

class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lessons')
    name = models.CharField(max_length=250)
    title = models.CharField(max_length = 200, null=True)
    position = models.PositiveSmallIntegerField(verbose_name="Hymn.")
    slug = models.SlugField(max_length=90, null=True, blank=True)
    body = models.TextField(max_length=50, null=True, blank=True)
    body2 = models.TextField(max_length=50, null=True, blank=True)
    body3 = models.TextField(max_length=50, null=True, blank=True)
    body4 = models.TextField(max_length=50, null=True, blank=True)
    body5 = models.TextField(max_length=50, null=True, blank=True)
    body6 = models.TextField(max_length=50, null=True, blank=True)
    body7 = models.TextField(max_length=50, null=True, blank=True)
    body8 = models.TextField(max_length=50, null=True, blank=True)
    body9 = models.TextField(max_length=50, null=True, blank=True)
    body10 = models.TextField(max_length=50, null=True, blank=True)
    body11 = models.TextField(max_length=50, null=True, blank=True)
    body12 = models.TextField(max_length=50, null=True, blank=True)
    body13 = models.TextField(max_length=50, null=True, blank=True)
    body14 = models.TextField(max_length=50, null=True, blank=True)
    body15 = models.TextField(max_length=50, null=True, blank=True)
    body16 = models.TextField(max_length=50, null=True, blank=True)
    body17 = models.TextField(max_length=50, null=True, blank=True)
    body18 = models.TextField(max_length=50, null=True, blank=True)
    body19 = models.TextField(max_length=50, null=True, blank=True)
    body20 = models.TextField(max_length=50, null=True, blank=True)
    body21 = models.TextField(max_length=50, null=True, blank=True)
    body22 = models.TextField(max_length=50, null=True, blank=True)
    body23= models.TextField(max_length=50, null=True, blank=True)
    body24 = models.TextField(max_length=50, null=True, blank=True)
    body25 = models.TextField(max_length=50, null=True, blank=True)
    body26 = models.TextField(max_length=50, null=True, blank=True)
    body27 = models.TextField(max_length=50, null=True, blank=True)
    body28 = models.TextField(max_length=50, null=True, blank=True)
    body29 = models.TextField(max_length=50, null=True, blank=True)
    body30 = models.TextField(max_length=50, null=True, blank=True)
    body31 = models.TextField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['position']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)  
        
    def get_absolute_url(self):
        return reverse('church:lesson_list', kwargs={'slug':self.subject.slug, 'standard':self.Standard.slug})



class SundaySermon(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    name = models.CharField(max_length=250, null=True)
    name2 = models.CharField(max_length=250, null=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
class DCCYearlyProgram(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    name = models.CharField(max_length=250, null=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title

class ChildrenSundaySchool(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    name = models.CharField(max_length=250, null=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title

class AdultSundaySchool(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    name = models.CharField(max_length=250, null=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    body4 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
class DonateMoney(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    name = models.CharField(max_length=250, null=True)
    name2 = models.CharField(max_length=250, null=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title

class WeeklyPrayersMotivations(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    body1 = models.TextField(max_length=500, null=True, blank=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    body3 = models.TextField(max_length=500, null=True, blank=True)
    body4 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title


class WeeklyGiveAway(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    body = models.TextField(max_length = 500)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title

class HistoryOfBabalola(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    
class HistoryOfCAC(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200)
    name = models.CharField(max_length=250, null=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
