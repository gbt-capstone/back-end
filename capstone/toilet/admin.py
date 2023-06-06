from django.contrib import admin
from .models import Toilet, Review

# Register your models here.
@admin.register(Toilet)
class ToiletAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass