from django.urls import path
from .views import MovieListCreateView
from .views import MovieRetrieveUpdateDestroyView
from .views import MovieStatisticsView

urlpatterns = [
    path('movies/', MovieListCreateView.as_view(), name='movies_list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movies_retrieve'),
    path('movies/stats/', MovieStatisticsView.as_view(), name='movie-stats'),
]