from django.shortcuts import render, redirect
from .models import Contacts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    contacts = Contacts.objects.filter(user_id=request.user)
    return render(request,"home.html",{'contacts':contacts})

def signupuser(request):
    if request.method == 'GET':
        userform = UserCreationForm()
        return render(request, 'signupuser.html',{'form':userform})
    else:
        userform = UserCreationForm(request.POST)
        userform.save()
        return redirect('home')

def loginuser(request):
    authform = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'loginform.html', {'form':authform})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(user.get_username())
            return redirect('home')
        else:
            return render(request,'loginform.html', {'form':authform, 'error':'invalid login try again'})

def logoutuser(request):
    logout(request)
    return render(request, 'home.html', {'message':'logout successful'})
    