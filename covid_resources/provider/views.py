from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'provider\index.html')

def pform(request):
    return render(request, 'provider\provider_form.html')

def pdata(request):
    return render(request, 'providerprovider_data.html')