from django.urls import path
from eventapp.views import events

urlpatterns = [
    path('<str:month>/', events),
]
