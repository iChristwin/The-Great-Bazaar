from django import forms
from django.template.loader import render_to_string

from django.forms import ModelForm
from .models import Item, CloudinaryItemPhoto

# ===================================================================


class ItemForm(forms.ModelForm):
    iTemplate = 'items/item_description.txt'
    description = forms.CharField(help_text="**Add information that more accurately Describes your Item",
                                  initial=render_to_string(iTemplate).strip(),
                                  widget=forms.Textarea(attrs={'cols': 35, 'rows': 4, }),
                                  )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description',)
        labels = {'name': 'Item name', }


class CloudinaryPhotoForm(ModelForm):
    class Meta:
        model = CloudinaryItemPhoto
        fields = ('image', )
