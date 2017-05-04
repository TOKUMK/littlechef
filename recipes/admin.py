from django.contrib import admin
from .models import Recipe, RecipeStep, RecipeStepIngredient, Ingredient, IngredientType

admin.site.register(Recipe)
admin.site.register(RecipeStep)
admin.site.register(RecipeStepIngredient)
admin.site.register(Ingredient)
admin.site.register(IngredientType)
