from django.urls import path
from provider import views

app_name = 'provider'

urlpatterns = [
    path('pform/', views.pform, name='pform'),
    path('pdata/', views.pdata, name='pdata'),
]
