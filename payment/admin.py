from django.contrib import admin

# Register your models here.
from .models import Accounts, CollectDeposit, DisburseDeposit


class CollectDepositAdmin(admin.ModelAdmin):
    model = CollectDeposit


class DisburseDepositAdmin(admin.ModelAdmin):
    model = DisburseDeposit


class AccountsAdmin(admin.ModelAdmin):
    model = Accounts


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(CollectDeposit, CollectDepositAdmin)
admin.site.register(DisburseDeposit, DisburseDepositAdmin)
