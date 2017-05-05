from django.conf.urls import url, include

from . import views

urlpatterns = [
	# anything coming in under url /recipes/ returns the index template. 
	url(r'^$', views.index, name='index'),


	# (url, view to return, url name for reverse url function and quick access)
	url(r'^recipes/$', views.RecipeListView.as_view(), name='recipes'),
	
	# how exactly is the regex working here. how does django generate pk at model level.
	url(r'^recipes/(?P<pk>\d+)$', views.RecipeDetailView.as_view(), name='recipe-detail'),

	#url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
	#url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]
