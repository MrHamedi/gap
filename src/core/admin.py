from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomeUser
from .forms import UserCreationForm


class CustomeUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = CustomeUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']
    form = UserCreationForm


admin.site.register(CustomeUser, CustomeUserAdmin)
