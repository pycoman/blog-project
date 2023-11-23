from django.urls import path
from .views import blogView, blogDetailView


urlpatterns = [
    path('', blogView.as_view(), name='home'),
    path('post/<int:pk>/', blogDetailView.as_view(), name='blog-detail'),
]

