from django.db import models


RATINGS = (
    ('5', '5 Star'),
    ('4', '4 Star'),
    ('3', '3 Star'),
    ('2', '2 Star'),
    ('1', '1 Star'),
)

TYPE = (
    ('movie', 'movie'),
    ('series', 'series'),
    ('episode', 'episode'),
)


class Genre(models.Model):
    """Model definition for Genre."""

    name = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Genre."""

        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        """Unicode representation of Genre."""
        return self.name


class Movie(models.Model):
    """Model definition for Movie."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateField()
    rated = models.CharField(choices=RATINGS, max_length=1)
    duration = models.CharField(max_length=10)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True)
    actors = models.CharField(max_length=400)
    country = models.CharField(max_length=100)
    type = models.CharField(choices=TYPE,max_length=15)
    poster = models.ImageField()
    director = models.CharField(max_length=200)
    language = models.CharField(max_length=30)


    class Meta:
        """Meta definition for Movie."""

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of Movie."""
        return self.title
