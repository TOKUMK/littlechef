from django.db import models

# Create your models here.

class Recipe(models.Model):
	
	#recipe_id = (pk)

	recipe_name = models.CharField(max_length=200, help_text="Enter a recipe title")
	recipe_description = models.CharField(max_length=1000, help_text="enter a breif description of the recipe")
	

class RecipeSteps(models.Model):
	
	#recipe_id = (fk)
	step_number = models.IntegerField()
	instructions = models.CharField(max_length=400, help_text="Enter a instruction for recipe step")



class RecipeStepsIngredients(models.Model):

	#recipe_id = (fk)
	#step_number = (fk)
	#ingreditent_id = (fk) 
	amount_required = models.IntegerField()



class Ingredients(models.Model):
	
	#ingredient_id = (pk)
	#ingredient_type_code = (fk)
	ingredient_name = models.CharField(max_length=50, help_text="Enter an ingredient name")
	
	


class IngredientsType(models.Model):
	#ingredient_type_code = (pk)
	ingredient_type_description = models.CharField(max_length = 500, help_text="Enter a description of ingredient type")





