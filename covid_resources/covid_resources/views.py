from django.shortcuts import render


# Create your views here.



# def index(request):
#     return render(request, 'provider_form.html')


def index(request):
    return render(request, 'home.html')


def tnc(request):
    return render(request, 't&c.html')

def contact(request):
    return render(request, 'contact.html')

def res(request):
    return render(request, 'resources.html')
