from django.contrib import admin

from .models import Server, Channel, Category
# Register your models here.
admin.register(Channel)
admin.register(Category)
admin.register(Server)
