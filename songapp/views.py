from django.shortcuts import render
from songapp.models import Song
from django.utils import timezone


def index(request):
    day = timezone.now()
    month = str(day.year) + '-' + str(day.month)
    return render(request, 'songapp/index.html', {'month': month})


def song(request):
    # index view
    songs = Song.objects.only('title').order_by('title')
    context = {
        'songs': songs,
    }
    return render(request, 'songapp/song.html', context)


def lyrics(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'songapp/lyrics.html', {'song': song})
