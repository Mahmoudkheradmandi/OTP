
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otp/' , include('otp.urls')),
    path('otp-drf/' , include('otp_drf.urls')),
]
