from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def tnc(request):
    return render(request, 't&c.html')

