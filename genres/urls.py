from django.urls import path
from .views import GenreListCreateView
from .views import GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genres_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres_list')
]