from django.contrib import admin

from .models import DietProduct, BreakfastProduct, LunchProduct, SupperProduct

admin.site.register(DietProduct)
admin.site.register(BreakfastProduct)
admin.site.register(LunchProduct)
admin.site.register(SupperProduct)