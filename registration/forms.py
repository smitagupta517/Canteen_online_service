# from django.contrib.auth import (
#     authenticate,
#     get_user_model,
#     login,
#     logout,
#     )
# from django import forms
#
#
# User = get_user_model()
#
#
# class UserForm(forms.Form):
#     username = forms.CharField(max_length=15)
#     password = forms.CharField(widget=forms.PasswordInput, min_length=8)
#
#     def clean(self, *args, **kwargs):
#         username = self.cleaned_data.get("username")
#         password = self.cleaned_data.get("password")
#
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if not user:
#                 raise forms.ValidationError("Invalid User")
#             if not user.check_password(password):
#                 raise forms.ValidationError("Incorrect Password")
#             if not user.is_active:
#                 raise forms.ValidationError("User is no longer active")
#         return super(UserForm, self).clean(*args, **kwargs)
#
#
# class UserRegistrationForm(forms.ModelForm):
#     username = forms.CharField(label="Username")
#     email = forms.EmailField(label="Email Address")
#     password = forms.CharField(widget=forms.PasswordInput, min_length=8)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#         ]
#
#     def clean_password2(self):
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password != password2:
#             raise forms.ValidationError("Password doesn't match")
#         return password

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Username',
        max_length=32,
    )
    email = forms.CharField(
        required=True,
        label='Email',
        max_length=32,
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=32,
        widget=forms.PasswordInput()
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        required=False,
        help_text='Optional',
    )
    last_name = forms.CharField(
        max_length=50,
        required=False,
        help_text='Optional',
    )
    email = forms.EmailField(
        max_length=20,
        help_text='Required. Invalid Email address',
    )


class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
