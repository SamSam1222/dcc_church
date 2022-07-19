from django import forms
from .models import SundaySermon, DCCYearlyProgram, ChildrenSundaySchool, AdultSundaySchool, DonateMoney, WeeklyPrayersMotivations, WeeklyGiveAway, HistoryOfBabalola, HistoryOfCAC



class Sunday(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = SundaySermon
        fields = ('image', 'title', 'name', 'name2', 'body', 'body2', 'body3')
        

class Program(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = DCCYearlyProgram
        fields = ('image', 'title', 'name', 'body', 'body2')

class Children(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = ChildrenSundaySchool
        fields = ('image', 'title', 'name', 'body', 'body2')
class Adult(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = AdultSundaySchool
        fields = ('image', 'title', 'name', 'body', 'body2')

class Donate(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = DonateMoney
        fields = ('image', 'title', 'name', 'name2')

class Motivation(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = WeeklyPrayersMotivations
        fields = ( 'image', 'title', 'body1', 'body2', 'body3', 'body4')

class GiveAway(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = WeeklyGiveAway
        fields = ( 'image', 'title', 'body')

class History(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = HistoryOfBabalola
        fields = ( 'image', 'title', 'name')

class Cac(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = HistoryOfCAC
        fields = ( 'image', 'title', 'name')
