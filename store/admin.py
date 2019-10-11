from django.contrib import admin

# Register your models here.
# My imports -----------------------------------------------------------------
from .models import Store, Stock


class StoreAdmin(admin.ModelAdmin):
    model = Store
    list_display = ('name', 'owner', 'is_verified', )


class StockAdmin(admin.ModelAdmin):
    model = Stock
    list_display = ('name', 'category', 'quantity', 'price', 'pk', )


admin.site.register(Store, StoreAdmin)
admin.site.register(Stock, StockAdmin)
