from django.contrib import admin

# Register your models here.
# My imports -----------------------------------------------------------------
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ('user__{0}'.format('username'),
                     'user__first_name', 'user__last_name')
    list_display = ('username', 'alias', 'locale', 'is_active', 'is_staff', 'gender', 'pk')


admin.site.register(User, UserAdmin)
