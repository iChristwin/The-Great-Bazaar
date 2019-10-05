from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)
        labels = {'username': 'Mobile Number (with country code)', }


class ProfileForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('alias', 'locale', 'acc_no', 'email', 'gender',)
        labels = {'locale': 'Campus', 'acc_no': 'Bank Account Number'}
        widgets = {'email': forms.Textarea(
                        attrs={'rows': 1,
                               'placeholder': 'An email address helps in account validation & recovery'
                           }
                        ),
                   }
