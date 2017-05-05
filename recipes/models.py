from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Recipe(models.Model):
	
	#recipe_id = pk

	recipe_name = models.CharField(max_length=200, help_text="Enter a recipe title")
	recipe_description = models.CharField(max_length=1000, help_text="enter a breif description of the recipe")

	def __str__(self):
		return '%s' % (self.recipe_name)

	def get_absolute_url(self):
		return reverse('recipe-detail', args=[str(self.id)])

    
	

class RecipeStep(models.Model):
	
	#recipe_id = (fk)
	recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
	step_number = models.IntegerField()
	instructions = models.CharField(max_length=400, help_text="Enter a instruction for recipe step")

	def __str__(self):

		return '%s Step: %s' % (self.recipe.recipe_name, self.step_number)





class RecipeStepIngredient(models.Model):

	#recipe_id = (fk)
	#step_number = (fk)
	#ingreditent_id = (fk) 

	recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
	recipe_step = models.ForeignKey('RecipeStep', on_delete=models.SET_NULL, null=True)
	ingredient = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)

	amount_required = models.IntegerField()

	def __str__(self):
		return '%s' % (self.ingredient.ingredient_name)



class Ingredient(models.Model):
	
	#ingredient_id = (pk)

	ingredient_type = models.ForeignKey('IngredientType', on_delete=models.SET_NULL, null=True)

	ingredient_name = models.CharField(max_length=50, help_text="Enter an ingredient name")
	def __str__(self):
		return '%s' % (self.ingredient_name)
	
	


class IngredientType(models.Model):
	#ingredient_type_code = (pk)

	ingredient_type_description = models.CharField(max_length = 500, help_text="Enter a description of ingredient type")

	def __str__(self):
		return '%s' % (self.ingredient_type_description)





