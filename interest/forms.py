from django import forms

from .models import Offer, Bargain, Order

# ===================================================================


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('offer',)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)


class BargainForm(forms.ModelForm):
    class Meta:
        model = Bargain
        fields = ('bargain',)
