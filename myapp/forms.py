from django import forms
from django.forms import ModelForm
from .models import Contacts

class Contactform(ModelForm):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'phone_number', 'image', 'user']
        widgets = {'user': forms.HiddenInput()}
