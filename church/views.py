from telnetlib import DO
from weakref import WeakKeyDictionary
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, DetailView, 
                                  ListView)
from .models import Standard, Subject, Lesson, SundaySermon, DCCYearlyProgram, ChildrenSundaySchool, AdultSundaySchool, DonateMoney, WeeklyPrayersMotivations, WeeklyGiveAway, HistoryOfBabalola, HistoryOfCAC

def index(request):
    return render(request,'base.html')

# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'church/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'church/subject_list_view.html'
    
    
class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'church/lesson_list_view.html'
    
    
class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'church/lesson_detail_view.html'
    

def Sunday(request):
    teachs = SundaySermon.objects.all()
    return render(request, 'church/Sunday.html', {'teach': teachs})

def Program(request):
    love2 = DCCYearlyProgram.objects.all()
    return render(request, 'church/Program.html', {'love': love2})

def Children(request):
    food2 = ChildrenSundaySchool.objects.all()
    return render(request, 'church/Children.html', {'food': food2})

def Adult(request):
    men2 = AdultSundaySchool.objects.all()
    return render(request, 'church/Adult.html', {'men': men2})

def Donate(request):
    money2 = DonateMoney.objects.all()
    return render(request, 'church/Donate.html', {'money': money2})

def Motivation(request):
    motivation2 = WeeklyPrayersMotivations.objects.all()
    return render(request, 'church/Motivation.html', {'motivation': motivation2})

def GiveAway(request):
    GiveAway2 = WeeklyGiveAway.objects.all()
    return render(request, 'church/GiveAway.html', {'GiveAway': GiveAway2})

def History(request):
    History2 = HistoryOfBabalola.objects.all()
    return render(request, 'church/History.html', {'History': History2})

def Cac(request):
    cac2 = HistoryOfCAC.objects.all()
    return render(request, 'church/Cac.html', {'cac': cac2})
