from django import forms

from .models import UserReview


class UserReviewForm(forms.ModelForm):
    model = UserReview
    fields = ('rating', 'comment', )
