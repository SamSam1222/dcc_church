from django.contrib import admin
from blogapp.models import UserProfileInfo
from .models import Blog_Post, Comment, AboutUs, UpcomingEvents

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
class AboutUsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}

class UpcomingEventsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
admin.site.register(Blog_Post, BlogPostAdmin)
admin.site.register(Comment)
admin.site.register(UserProfileInfo)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(UpcomingEvents, UpcomingEventsAdmin)
