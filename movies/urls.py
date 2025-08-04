from django.urls import path
from .views import MovieListCreateView
from .views import MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movies_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movies_retrieve')
]