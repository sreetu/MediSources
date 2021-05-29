from django.urls import path
from consumer import views

app_name =  'consumer'

urlpatterns = [
    path('cform/', views.cform, name='cform'),
    path('cdata/', views.cdata, name='cdata'),
]
