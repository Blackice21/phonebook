from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth import authenticate, get_user, login, logout
from django.contrib.auth.decorators import login_required
from .forms import Contactform

# Create your views here.
def create_contact(request):
    if request.method == 'GET':
        form = Contactform(initial={'user': request.user})
        print(form['user'])
        return render(request, 'crud/create_contact.html', {'form': form})
    else:
        form = Contactform(request.POST, request.FILES)
        form.save()
        return redirect('home')

def detail_contact(request, pk):
    contact = get_object_or_404(Contacts, pk=pk)
    return render(request, 'crud/detail.html', {'contact': contact})     

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
    