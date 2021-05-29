from django.urls import path
from .views import cform, cdata, createrequest, login

app_name =  'consumer'

urlpatterns = [
<<<<<<< HEAD
    path('cform/', cform, name='cform'),
    path('cdata/', cdata, name='cdata'),
    path('createrequest/', createrequest, name='createrequest'),
    path('login/', login, name='login')
=======
    path('cindex/',views.cindex,name='cindex'),
    path('cform/', views.cform, name='cform'),
    path('cdata/', views.cdata, name='cdata'),
>>>>>>> 08434a96f6d312d327bdab17b88856688fdc60b4
]
