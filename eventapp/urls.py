from django.urls import path
from eventapp.views import events

urlpatterns = [
    path('evenements/<str:month>/', events),
]
