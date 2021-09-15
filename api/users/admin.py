from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib.auth.admin import UserAdmin

class NewUserAdmin(UserAdmin):
    fieldsets = (
            (None, {'fields': ('email', 'first_name', 'last_name', 'is_active', 'date_of_birth', 'is_staff', 'password')}),
    )

admin.site.register(User, NewUserAdmin)