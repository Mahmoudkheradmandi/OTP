from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin): 
    pass

class AdminOTPRequest(admin.ModelAdmin): 
    
        model = OTPRequest
        list_display = ['request_id','created', 'password','receiver' , 'channel']

admin.site.register(User , UserAdmin)
admin.site.register(OTPRequest , AdminOTPRequest)


