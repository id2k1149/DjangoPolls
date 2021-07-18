from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Question, VoteCounter


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class QuestionForm(forms.ModelForm):
    title = forms.CharField(label='Question',
                            widget=forms.TextInput(attrs={'placeholder': 'Question', 'class': 'form-control'}))

    answers = forms.ModelMultipleChoiceField(label='Options',
                                             queryset=VoteCounter.objects.all(),
                                             widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Question
        fields = ('title', 'answers')
