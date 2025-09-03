from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError
from rest_framework.serializers import SerializerMethodField
from django.db.models import Avg
from .models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer



class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validade_resume(self, value):
        if len(value) > 300:
            raise ValidationError('Só é permitido criar um resumo de no máximo 300 caracteres!')
        else:
            return value


class MovieModelSerializer(ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer()
    rate = SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(
            avg_value=Avg('stars')
        )['avg_value']

        return round(rate, 1) if rate else None
