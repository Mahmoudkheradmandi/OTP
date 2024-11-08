from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render , redirect
from django.views import generic
from random import randint
from django.contrib.auth import get_user_model , login as lo
from django.contrib import messages



class index(generic.TemplateView): 
    template_name = 'index.html' 


class login(generic.TemplateView): 
    otp = ''
    phone_number = ''
    
    def get(self, request, *args, **kwargs):
        login.phone_number = request.GET.get('phone_number')
        context = {
            'method' : 'get'
        }
        login.otp = str(randint(100000 , 999999))
        messages.success(request , login.otp)
        return render(request , 'login.html' , context)
    
    def post(self, request, *args, **kwargs):
        sent_otp = request.POST.get('sent_otp')
        if sent_otp==login.otp:
            user = get_user_model().objects.filter(username = login.phone_number).first()
            if user: 
                lo(request , user) 
            else:  
                new_user = get_user_model().objects.create(username = login.phone_number)
                lo(request , new_user)
                print('ok')
            return redirect('index')     
        else: 
            print('otp code is not match')        
        context = {
            'method' : 'post'
        }
        return render(request , 'login.html' , context)


