from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=80, label='Username', widget=forms.TextInput(attrs=
                                                                                       {'class': 'form-control'}))
    password = forms.CharField(max_length=80, label='Password', widget=forms.PasswordInput(attrs=
                                                                                       {'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=80, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=80, label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=80, label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=150, label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=150, label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(max_length=150, label='E-mail',
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
