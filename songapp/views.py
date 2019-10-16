from django.shortcuts import render


def index(request):
    # index view
    return render(request, 'songapp/index.html')
