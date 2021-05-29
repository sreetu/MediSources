from django.shortcuts import render

# Create your views here.


def pform(request):
    return render(request, 'provider_form.html')

def pdata(request):
    return render(request, 'provider_data.html')