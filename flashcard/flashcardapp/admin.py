from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    display_fields = [field.name for field in Card._meta.get_fields()]


class CardAdmin(admin.ModelAdmin):
    display_fields = [field.name for field in Card._meta.get_fields()]

class CardMistakenAdmin(admin.ModelAdmin):
    display_fields = [field.name for field in CardMistaken._meta.get_fields()]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(CardMistaken, CardMistakenAdmin)
