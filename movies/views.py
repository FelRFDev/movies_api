from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count
from django.db.models import Avg
from core.permissions import GlobalDefaultPermission
from .models import Movie
from reviews.models import Review
from .serializers import MovieSerializer
from .serializers import MovieModelSerializer



# Create your views here.
class MovieListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieModelSerializer
        else:
            return MovieSerializer

class MovieRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieStatisticsView(APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission)
    queryset = Movie.objects.all()

    def get(self):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(Avg('stars'))['stars__avg']
    
        return Response(
            data={
                'total_movies':total_movies,
                'movies_by_genre':movies_by_genre,
                'total_reviews':total_reviews,
                'average_stars':round(average_stars, 1) if average_stars else 0
            },
            status=HTTP_200_OK
        )