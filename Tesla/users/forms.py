from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    username = forms.CharField(disabled=True, required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'name', 'email', 'gender']
        widgets = {
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.user.username:
            self.initial['user'] = self.instance.user.username

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))