from django.urls import path
from .views import *

app_name =  'consumer'

urlpatterns = [
    path('cform/', cform, name='cform'),
    path('cdata/', cdata, name='cdata'),
    path('createrequest/', createrequest, name='createrequest'),
    path('cindex/', cindex, name='cindex'),
    path('ctable/', ctable, name='ctable'),
]
