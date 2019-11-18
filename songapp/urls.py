from django.urls import path
from songapp import views


urlpatterns = [
    path('', views.song, name='song'),
    path('paroles-<int:song_id>/', views.lyrics),
]
