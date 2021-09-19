from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import fields
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
      model = Contact
      fields = ['name','email','message']