from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Consumer, Request

# Create your views here.


def cindex(request):
    if request.method== 'POST':
        name = request.POST['username']
        dob = request.POST['dob']
        consumer = Consumer.objects.filter(phone=name,dob=dob)
        if consumer:
            requests=Request.objects.filter(consumer_id=consumer[0].pk)
            # request.session['requests']=requests
            # request.session['user'] = consumer[0]
            print(requests)
            return render(request, 'consumer\consumer_data.html', {'consumer': consumer[0],'requests': requests})
        else:
            return render(request, 'consumer\cindex.html', {'messages': 'Invalid User Details'})
    else:
        return render(request, 'consumer\cindex.html')

def ctable(request):
    requests=Request.objects.all()
    return render(request, 'provider\provider_table.html',{ 'requests':requests})

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


def createrequest(request):
    if request.method == 'POST':
        consumer = Consumer.objects.get(pk=request.user.id)
        type = request.POST['type']
        count = request.POST['count']
        return HttpResponse('success')
    else:
        return HttpResponse('error')
