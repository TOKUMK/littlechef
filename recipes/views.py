from django.shortcuts import render
from django.views import generic
from .models import Recipe


# Create your views here.

# Function vs class based views


# index view to serve initial page
# function based view
def index(request):

	"""
	View function for home page of site.
   
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
	"""

	return render(
		request,
		'index.html',
		context={'num_recipes':10,'num_chefs':5,'num_recipe_types':8,'num_ingredients':500},)

# CLass based views
# how exactly is this working. ?Name convention and arg param ?
class RecipeListView(generic.ListView):
	model = Recipe

# todo: how to make this more customisable.
class RecipeDetailView(generic.DetailView):
	model = Recipe


