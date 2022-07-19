from django.urls import path
from . import views

app_name='church'
urlpatterns = [
    path('', views.StandardListView.as_view(), name="standard_list"),
    path('Sunday/', views.Sunday, name='Sunday'),
    path('Program/', views.Program, name='Program'),
    path('Children/', views.Children, name='Children'),
    path('Adult/', views.Adult, name='Adult'), 
    path('Donate/', views.Donate, name='Donate'), 
    path('GiveAway/', views.GiveAway, name='GiveAway'), 
    path('Motivation/', views.Motivation, name='Motivation'), 
    path('History/', views.History, name='History'), 
    path('Cac/', views.Cac, name='Cac'), 
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:standard>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:standard>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(),name='lesson_detail'),
      
]