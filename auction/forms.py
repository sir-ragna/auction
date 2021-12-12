from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django import forms

"""
Authentication forms based upon the default user model.
User model doc: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
Django Auth doc: https://docs.djangoproject.com/en/3.2/topics/auth/default/
"""

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, validators=[validate_password])
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

