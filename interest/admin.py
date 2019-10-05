from django.contrib import admin

# Register your models here.
# My imports -----------------------------------------------------------------
from .models import Offer, Bargain, Bookmarks


class OfferAdmin(admin.ModelAdmin):
    model = Offer
    search_fields = ('owner__{0}'.format('username'), 'item__name', 'item__category', 'pk')
    list_display = ('owner', 'item', 'pk', 'offer', 'accepted')


class BargainAdmin(admin.ModelAdmin):
    model = Bargain
    search_fields = ('seller', 'offer__item__name', 'pk')
    list_display = ('seller', 'offer', 'bargain', )


class BookmarkAdmin(admin.ModelAdmin):
    model = Bookmarks
    list_display = ('owner',)


admin.site.register(Offer, OfferAdmin)
admin.site.register(Bargain, BargainAdmin)
admin.site.register(Bookmarks, BookmarkAdmin)
