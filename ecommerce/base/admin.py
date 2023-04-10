from django.contrib import admin
from .models import Country, Image, Item, UserProfile, Order

admin.site.register(Country)
admin.site.register(Image)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(UserProfile)