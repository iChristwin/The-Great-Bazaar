from django import forms
from django.template.loader import render_to_string

from .models import Item

# ===================================================================


class ItemForm(forms.ModelForm):
    iTemplate = 'items/item_description.txt'
    description = forms.CharField(help_text="**Add information that more accurately Describes your Item",
                                  initial=render_to_string(iTemplate).strip(),
                                  widget=forms.Textarea(attrs={'cols': 35, 'rows': 4, }),
                                  )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'photo_front', 'photo_back')
        labels = {'name': 'Item name', 'photo_front': 'Item image (front)',
                  'photo_back': 'Item image (other)', }

