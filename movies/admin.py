from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','genre','release_date')
    list_filter = ('release_date',)
    search_fields = ('title', 'release_date')
