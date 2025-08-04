from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=(MaxValueValidator(5), MinValueValidator(0)))
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.movie
