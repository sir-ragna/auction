from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User
from django import forms

"""
Authentication forms based upon the default user model.
User model doc: https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User
Django Auth doc: https://docs.djangoproject.com/en/3.2/topics/auth/default/
"""

# class UserLoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'username': TextInput(
#                 attrs={"placeholder":"username", "class":"form-control"}
#             ),
#             'password': PasswordInput(attrs={"class": "form-control"}),
#         }

class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

        # def clean_password(self):
        #     password = self.cleaned_data['password']
        #     if password == '':
        #         raise forms.ValidationError("A password must be provided")
        #     if len(password) < 8:
        #         print("minimum length not reached")
        #         raise forms.ValidationError("Minimum length is 8 characters")
            # return self.cleaned_data['password']
