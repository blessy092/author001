
from . import views
from django.urls import path
app_name ='demoapp'

urlpatterns = [
    
    path('',views.demof,name='demof'),
    path('add/',views.addition,name="addition"),
    path('register/',views.addregister,name='addregister'),
    path('addlogin',views.addlogin,name='addlogin'),
    path('logout/',views.logout,name='logout'),
    path('addregister/',views.register,name='register'),
    path('about/',views.aboutf,name='aboutf')
    
   
    
]
