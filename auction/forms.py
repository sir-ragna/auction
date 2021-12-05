from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User

"""
Authentication forms based upon the default user model.
User model doc: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
Django Auth doc: https://docs.djangoproject.com/en/3.2/topics/auth/default/
"""

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(
                attrs={"placeholder":"username", "class":"form-control"}
            ),
            'password': PasswordInput(
                attrs={"class": "form-control"}
            ),
        }

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
