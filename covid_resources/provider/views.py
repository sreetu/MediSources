from .models import Provider, Resource
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def pindex(request):
    return render(request, 'provider\pindex.html')

def login(request):
    name = request.POST['name']
    dob = request.POST['dob']
    provider = Provider.objects.get(name=name, dob=dob)
    if provider:
        return render(request, 'home.html', {'messages': 'Login Successful'})
    else: 
        return render(request, 'home.html', {'messages': 'Invalid User Details'})

def login(request):
    name = request.POST['name']
    dob = request.POST['dob']
    provider = Provider.objects.get(name=name, dob=dob)
    if provider:
        return render(request, 'home.html', {'messages': 'Login Successful'})
    else: 
        return render(request, 'home.html', {'messages': 'Invalid User Details'})

def pform(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        pincode = request.POST['pincode']
        email = request.POST['email']
        city = request.POST['city']
        deliver = request.POST['deliver']
        if (deliver == "YES"):
            provider = Provider(name=name, phone=phone, dob=dob, address=address, pincode=pincode, email=email, deliver=True, city=city)
        else:
            provider = Provider(name=name, phone=phone, dob=dob, address=address, pincode=pincode, email=email, city=city, deliver=False)
        provider.save()
        return render(request, 'home.html')
    else:
        return render(request, 'provider\provider_form.html')

def pdata(request):
    providers = Provider.objects.all()
    dict = {}
    for provider in providers:
        dict[provider.name] = Resource.objects.filter(provider_id=provider.pk)
    return render(request, 'provider\provider_data.html', {'providers': providers, 'dict': dict})
