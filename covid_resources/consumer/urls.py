from django.urls import path
from .views import cform, cdata, createrequest, login

app_name =  'consumer'

urlpatterns = [
    path('cform/', cform, name='cform'),
    path('cdata/', cdata, name='cdata'),
    path('createrequest/', createrequest, name='createrequest'),
    path('login/', login, name='login')
]
