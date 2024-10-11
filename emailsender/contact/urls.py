from django.urls import path, include
from . import views


urlpatterns = [
   
    path('', views.sendmail, name= 'contact'),
    path('success', views.success, name = 'success')
]
