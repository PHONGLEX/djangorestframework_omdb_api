from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend, filterset

from .models import Movie, Genre
from .serializers import MovieSerializer,GenreSerializer


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre__name', 'language', 'type']


class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = []


class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
    permission_classes = []


class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
