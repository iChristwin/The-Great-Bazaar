from django.contrib import admin

# Register your models here.
# My imports -----------------------------------------------------------------
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    search_fields = ('bidder__{0}'.format('username'), 'name',
                     'category', 'pk', 'available')
    model = Item
    list_display = ('name', 'category', 'available', 'owner', 'pk', )


admin.site.register(Item, ItemAdmin)
