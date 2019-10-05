from django import forms

from .models import Offer, Bargain

# ===================================================================


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('offer',)


class BargainForm(forms.ModelForm):
    class Meta:
        model = Bargain
        fields = ('bargain',)
