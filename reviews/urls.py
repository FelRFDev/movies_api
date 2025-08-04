from django.urls import path
from .views import ReviewListCreateView
from .views import ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='reviews_list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='reviews_retrieve')
]