from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import blogModel


class blogView(ListView):
    model = blogModel
    template_name = 'index.html'
    
    
class blogDetailView(DetailView):
    model = blogModel
    template_name = 'blog-detail.html'
    
    
    
