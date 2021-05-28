from django.shortcuts import render

# Create your views here.


def cform(request):
    return render(request, 'consumer_form.html')
