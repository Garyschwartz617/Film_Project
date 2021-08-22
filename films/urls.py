from django.urls import path
from . import views


urlpatterns = [
    path('homepage', views.homepage, name='home'),
    path('show_film', views.FilmListView.as_view(), name = 'all_films'),
    path('show_film/<int:pk>', views.FilmDetailView.as_view(), name = 'film_detail'),
    path('add_film', views.FilmCreateView.as_view(), name = 'create_film'),
    path('add_director', views.DirectorCreateView.as_view(), name = 'create_director'),
    path('add_country', views.CountryCreateView.as_view(), name = 'create_country'),
    path('add_category', views.CategoryCreateView.as_view(), name = 'create_category'),


]