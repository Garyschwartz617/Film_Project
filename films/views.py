from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .forms import MyFilmForm, PosterForm, CommentaryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages

# from braces import views

# Create your views here.

def homepage(request):
    films = Film.objects.all()

    return render(request,'homepage.html', {'films': films})

class FilmListView(ListView):
    model = Film
    ordering = 'title'
    template_name = ''
    
class FilmDetailView(DetailView):
    model = Film
    template_name = 'film/film.html'


# class FilmCreateView(CreateView):
#     model = Film
#     fields = '__all__'
#     template_name = 'film/addFilm.html'
#     success_url = reverse_lazy('home')


class CommentCreateView(CreateView):
    form_class = CommentaryForm
    template_name = 'film/addComment.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)





# @login_required
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

class FilmDeleteView(LoginRequiredMixin,DeleteView):
    model = Film
    template_name = 'film/deleteFilm.html'
    success_url = reverse_lazy('home')  
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        messages.warning(request,f'YOU JUST DELETED {self.object}')
        self.object.delete()
        return HttpResponseRedirect(success_url)
    
    
   
  