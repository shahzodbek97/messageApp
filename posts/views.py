from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'barcha_postlar'
class AboutPageView(ListView):
    model = Post
    template_name = 'about.html'
    context_object_name = 'barcha_postlar'