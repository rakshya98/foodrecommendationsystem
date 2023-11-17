from django.contrib import admin

from food_app.models import FoodItem, Rating

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Rating)