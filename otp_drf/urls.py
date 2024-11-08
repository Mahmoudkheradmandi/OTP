from . import views
from django.urls import path , include

urlpatterns = [
    
    path('otp' , views.OTPView.as_view() , name='view'),
]