from django.contrib import admin

# Register your models here.
# My imports -----------------------------------------------------------------
from .models import Item, CloudinaryItemPhoto


class ItemAdmin(admin.ModelAdmin):
    search_fields = ('bidder__{0}'.format('username'), 'name',
                     'category', 'pk', 'available')
    model = Item
    list_display = ('name', 'category', 'available', 'owner', 'pk', )


class CloudinaryPhotosAdmin(admin.ModelAdmin):
    model = CloudinaryItemPhoto
    list_display = ('item', 'pk',)


admin.site.register(Item, ItemAdmin)
admin.site.register(CloudinaryItemPhoto, CloudinaryPhotosAdmin)
