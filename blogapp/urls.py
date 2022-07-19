from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<str:slug>', views.blog_detailView, name = 'blog_detail'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('About/', views.About, name='About'),
    path('Events/', views.Events, name='Events'),
]


