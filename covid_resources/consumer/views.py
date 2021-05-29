from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Consumer, Request
# Create your views here.


def cindex(request):
    return render(request, 'consumer\cindex.html')

def login(request):
    name = request.POST['name']
    dob = request.POST['dob']
    consumer = Consumer.objects.get(name=name, dob=dob)
    if consumer:
        return render(request, 'home.html', {'messages': 'Login Successful'})
    else: 
        return render(request, 'home.html', {'messages': 'Invalid User Details'})

def cform(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        dob = request.POST['dob']
        address = request.POST['address']
        city = request.POST['city']
        pincode = request.POST['pincode']
        email = request.POST['email']
        severity = request.POST['severity']
        image = request.POST['image']
        consumer = Consumer(name=name, phone=phone, dob=dob, address=address, pincode=pincode, email=email, city=city)
        if severity == '1':
            consumer.severity = "mild"
        elif severity == '2':
            consumer.severity = "moderate"
        else:
            consumer.severity = "critical"
        consumer.save()
        return render(request, 'consumer\consumer_form.html')
    else:
        return render(request, 'consumer\consumer_form.html')

def cdata(request):
    requests = Request.objects.all()
    return render(request, 'consumer\consumer_data.html', {'requests': requests})

def createrequest(request):
    if request.method == 'POST':
        consumer = Consumer.objects.get(pk=request.user.id)
        type = request.POST['type']
        count = request.POST['count']
        return HttpResponse('success')
    else:
        return HttpResponse('error')
