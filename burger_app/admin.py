from django.contrib import admin

from .models import Burger

class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_image']

    def display_image(self, obj):
        return obj.image.url if obj.image else "No Image"
    display_image.short_description = 'Image'

admin.site.register(Burger, BurgerAdmin)
