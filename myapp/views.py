from django.shortcuts import render
from .models import Contacts
# Create your views here.
def home(request):
    contacts = Contacts.objects.all()
    return render(request,"home.html",{'contacts':contacts})