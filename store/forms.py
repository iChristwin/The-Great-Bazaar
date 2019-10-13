from django import forms
from django.template.loader import render_to_string
from django.forms import ModelForm

from .models import Store, Stock
from .models import CloudinaryPhoto

# ===================================================================


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('name', 'description', )
        labels = {'name': 'Store name', }


class StockForm(forms.ModelForm):
    iTemplate = 'items/item_description.txt'
    description = forms.CharField(help_text="**Add information that more accurately Describes your Item",
                                  initial=render_to_string(iTemplate).strip(),
                                  widget=forms.Textarea(attrs={'cols': 35, 'rows': 4, }),
                                  )

    class Meta:
        model = Stock
        fields = ('category', 'name', 'description', 'quantity', 'price')
        labels = {'name': 'Item name', }


class StockUpdateForm(StockForm):
    class Meta(StockForm.Meta):
        fields = ('category', 'name', 'description', 'quantity', 'price',)


class CloudinaryPhotoForm(ModelForm):
    class Meta:
        model = CloudinaryPhoto
        fields = ('image', )
