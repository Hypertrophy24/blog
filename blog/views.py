from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
# Create your views here.
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title","author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


    