from django.shortcuts import render
from .models import Blog_Post
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blogapp.forms import UserForm, UserProfileInfoForm
from django.views.generic import CreateView
from .models import UserProfileInfo, Contact, AboutUs, UpcomingEvents
from django.urls import reverse

def index(request):
    return render(request,'base.html')


# Create your views here.
def index(request):
    posts = Blog_Post.objects.all()
    return render(request,'index.html', {'posts': posts})


def blog_detailView(request, slug):
    post = Blog_Post.objects.get(slug = slug)
    comments = post.comments.all()
    new_comment = None
    
    
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args = [str(post.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'blog_detail.html', {'post': post, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})

    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
        
    else:
        return render(request, 'blogapp/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
# def index(request):
#     return render(request,'blogapp/index.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'blogapp/registration.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

class HomeView(TemplateView):
    template_name = 'blogapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ministers = UserProfileInfo.objects.filter(user_type='ministers')
        context['ministers'] = ministers
        return context

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'blogapp/contact.html'

def About(request):
    bodys = AboutUs.objects.all()
    return render(request,'blogapp/About.html', {'body': bodys})

def Events(request):
    posts2 = UpcomingEvents.objects.all()
    return render(request, 'blogapp/Events.html', {'post2': posts2})


