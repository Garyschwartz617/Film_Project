from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .forms import MyFilmForm, PosterForm
# Create your views here.

def homepage(request):
    films = Film.objects.all()

    return render(request,'homepage.html', {'films': films})

class FilmListView(ListView):
    model = Film
    ordering = 'title'
    
class FilmDetailView(DetailView):
    model = Film


# class FilmCreateView(CreateView):
#     model = Film
#     fields = '__all__'
#     template_name = 'film/addFilm.html'
#     success_url = reverse_lazy('home')








class FilmCreateView(CreateView):
    form_class = MyFilmForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['poster_form'] = PosterForm()
        return context

    def form_valid(self, form):
        poster_form = PosterForm(self.request.POST, self.request.FILES)
        if poster_form.is_valid():
            new_film = form.save()   
            poster = poster_form.save(commit=False)
            poster.film = new_film
            poster.save()
            return redirect('home')
        return self.form_invalid(form)    
       













class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('home')    

class CountryCreateView(CreateView):
    model = Country
    fields = '__all__'
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')    

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')   

class FilmUpdateView(UpdateView):
    model = Film
    fields = '__all__'
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')

class DirectorUpdateView(UpdateView):
    model = Director
    fields = '__all__'
    template_name = 'add/add.html'
    success_url = reverse_lazy('home')         