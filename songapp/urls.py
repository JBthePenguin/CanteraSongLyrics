from django.urls import path
from songapp import views
from eventapp.views import events

urlpatterns = [
    path('', views.index, name='index'),
    path('chansons/', views.song, name='song'),
    path('paroles-<int:song_id>/', views.lyrics),
    path('evenements/<str:month>/', events),
]
