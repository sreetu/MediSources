from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'consumer\index.html')

def cform(request):
    return render(request, 'consumer\consumer_form.html')

def cdata(request):
    return render(request, 'consumer\consumer_data.html')

