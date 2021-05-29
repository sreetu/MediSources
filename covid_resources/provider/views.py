from django.shortcuts import render

# Create your views here.
def pindex(request):
    return render(request, 'provider\pindex.html')

def pform(request):
    return render(request, 'provider\provider_form.html')

def pdata(request):
    return render(request, 'provider\provider_data.html')
