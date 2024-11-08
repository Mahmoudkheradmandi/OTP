
from django.urls import path , include
from . import views
urlpatterns = [
    
    path('' , views.index.as_view() , name='index'),
    path('login' , views.login.as_view() , name='login'),
]
