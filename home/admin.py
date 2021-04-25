from django.contrib import admin

# Register your models here.
from .models import Home

class Homeadmin(admin.ModelAdmin):
    model = Home


admin.site.register(Home, Homeadmin)