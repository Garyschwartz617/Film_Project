from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
# Create your views here.

def homepage(request):
    films = Film.objects.all()

    return render(request,'homepage.html', {'films': films})

class FilmListView(ListView):
    model = Film
    ordering = 'title'
    
class FilmDetailView(DetailView):
    model = Film


class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('home')

class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('home')    

class CountryCreateView(CreateView):
    model = Country
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')    

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    # form_class = AnimalForm
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')    