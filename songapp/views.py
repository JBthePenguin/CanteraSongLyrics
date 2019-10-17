from django.shortcuts import render
from songapp.models import Song


def index(request):
    # index view
    songs = Song.objects.only('title').order_by('title')
    return render(request, 'songapp/index.html', {'songs': songs})


def lyrics(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songapp/lyrics.html', {'song': song})
