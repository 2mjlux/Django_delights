from django.contrib import admin
from .models import Ingredient, MenuItem, RecipeRequirement, Sale


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Sale)
