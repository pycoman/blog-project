from django.shortcuts import render
from django.views.generic import ListView
from .models import blogModel


class blogView(ListView):
    model = blogModel
    template_name = 'index.html'
    
    
