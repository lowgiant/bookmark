from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    fields =['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields =['site_name', 'url']
    #update를 가져다 쓰게끔 하는 것. => 뒷부분만 바꾸어 주는 것
    template_name_suffix ='_update'
    success_url = reverse_lazy('list')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields =['site_name', 'url']
    template_name_suffix = '_delete'
    success_url = reverse_lazy('list')
