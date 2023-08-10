from django.shortcuts import render, get_object_or_404
from .models import Genre, Artist
# Create your views here.


def show_categories(request):
    genres = Genre.objects.all()

    return render(request, 'categories.html', {'genres': genres})


def show_all_artists(request, genre_name):
    genre = get_object_or_404(Genre, genre=genre_name)

    artists = Artist.objects.filter(genre=genre)

    return render(request, 'showArtists.html', {"artists":artists})


def show_more(request, genre_name, pk):
    artist = Artist.objects.get(pk=pk)
    return render(request, 'showArtist.html', {'artist': artist})



