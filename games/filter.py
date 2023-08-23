from django_filters import FilterSet
from .models import Game

class GameFilter(FilterSet):
    class Meta:
        model = Game
        fields = {
            'studio':['exact'],
            'publisher':['exact'],
            'genre':['exact'],
            'price':['exact', 'lte', 'gte'],
            'is_active':['exact']
        }