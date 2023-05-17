from django.contrib import admin
from .models import Toilet

# Register your models here.
@admin.register(Toilet)
class ToiletAdmin(admin.ModelAdmin):
    pass