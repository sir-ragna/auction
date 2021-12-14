from django.forms import ModelForm, TextInput, PasswordInput, Textarea, NumberInput
from django.contrib.auth.password_validation import validate_password
from django import forms

from . import models

"""
Authentication forms based upon the default user model.
User model doc: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
Django Auth doc: https://docs.djangoproject.com/en/3.2/topics/auth/default/
"""

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, validators=[validate_password])
    class Meta:
        model = models.User
        fields = ['username', 'email', 'first_name', 'last_name']

class ListingForm(ModelForm):
    class Meta:
        model = models.Listing
        fields = ['title', 'description', 'starting_bid']
        widgets = {
            'title': TextInput(attrs={"placeholder": "title", "class": "form-control"}),
            'description': Textarea(attrs={"class": "form-control"}),
            'starting_bid': NumberInput(attrs={"class": "form-control"})
        }