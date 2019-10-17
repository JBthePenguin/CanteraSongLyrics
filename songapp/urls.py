from django.urls import path
from songapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('paroles-<int:song_id>/', views.lyrics)
]
