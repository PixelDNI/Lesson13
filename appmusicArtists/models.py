from django.db import models
from django.db.models import CharField, TextField


# Create your models here.
class Genre(models.Model):
    genre = CharField(max_length=100)

    def __str__(self):
        return str(self.genre)

    def get_absolute_url(self):

        return f'{self.genre}/'


class Artist(models.Model):
    genre = models.ManyToManyField(Genre)
    name = CharField(max_length=100)
    surname = CharField(max_length=100)
    age = CharField(max_length=100)
    brief_biography = TextField()


    def __str__(self):
        genre = ', '.join(str(genre) for genre in self.genre.all())
        return f"{self.name} - {self.surname} -{self.age} - {genre}"

    def get_absolute_url(self):
        return f'{self.id}/'
