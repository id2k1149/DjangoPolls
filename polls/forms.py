from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Letters and digits',
                                                             'class': "form-control rounded-0"}))

    password1 = forms.CharField(label='Password:',
                                widget=forms.TextInput(attrs={'placeholder': 'At least 8 characters',
                                                              'class': "form-control rounded-0"}))
    password2 = forms.CharField(label='Password confirmation:',
                                widget=forms.TextInput(attrs={'class': "form-control rounded-0"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
