from django.shortcuts import render
from songapp.models import Song
from django.utils import timezone


DAY = timezone.now()
MONTH = str(DAY.year) + '-' + str(DAY.month)


def index(request):
    context = {
        'month_navbar': MONTH,
    }
    return render(request, 'songapp/index.html', context)


def song(request):
    songs = Song.objects.only('title').order_by('title')
    context = {
        'song_navbar': "active",
        'songs': songs,
        'month_navbar': MONTH,
    }
    return render(request, 'songapp/song.html', context)


def lyrics(request, song_id):
    song = Song.objects.get(id=song_id)
    context = {
        'song_navbar': "active",
        'song': song,
        'month_navbar': MONTH,
    }
    return render(request, 'songapp/lyrics.html', context)


def error_404(request, exception):
    return render(request, 'error/404.html', status=404)
