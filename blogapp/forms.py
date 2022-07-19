from django import forms
from .models import Comment
from .models import AboutUs
from .models import UpcomingEvents
from django.contrib.auth.models import User
from blogapp.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class About(forms.ModelForm):
    body = forms.CharField(max_length=100, required=False )
    class Meta:
        model = AboutUs
        fields = ('image', 'title', 'body')

class Events(forms.ModelForm):
    body = forms.CharField(max_length= 100, required=False)
    class Meta:
        model = UpcomingEvents
        fields = ('image', 'title', 'body')
        

class CommentForm(forms.ModelForm):
    Commenter = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your name'
        }))
    body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Comment here', 'rows':3
    }))
    class Meta:
        model = Comment
        fields = ['Commenter', 'body']
        


class UserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        
        
        
        
        labels = {
            'password1':'Password',
            'password2':'Confirm Password'
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    ministers = 'ministers'
    members = 'members'
    user_types = [
        (ministers, 'ministers'),
        (members, 'members'),
    ]
    user_type = forms.ChoiceField(required=True, choices=user_types)
    
    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
    
