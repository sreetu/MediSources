from django.shortcuts import render

# Create your views here.


def cform(request):
    return render(request, 'consumer_form.html')



def consumer_data(request):
    return render(request, 'consumer_data.html')

