from django.urls import path
from .views import ActorListCreateView
from .views import ActorRetrieveUpdateDestroyView

urlpatterns = [
    path('actors/', ActorListCreateView.as_view(), name='actors_list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actors_retrieve')
]