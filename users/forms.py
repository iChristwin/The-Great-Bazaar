from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from .models import User


class UserForm(UserCreationForm):
    username = forms.CharField(initial='+234', label='Mobile Number (with country code)')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'acc_no',)
        labels = {'username': 'Mobile Number (with country code)',
                  'acc_no': 'Bank Account Number'}


class ProfileForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ('alias', 'locale', 'acc_no', 'email', 'gender',)
        labels = {'locale': 'Campus', 'acc_no': 'Bank Account Number',
                  'alias': 'Username', }
        widgets = {'email': forms.Textarea(
                        attrs={'rows': 1,
                               'placeholder': 'An email address helps in account validation & recovery'
                           }
                        ),
                   }
