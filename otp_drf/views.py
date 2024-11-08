from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status, views, mixins

from rest_framework.views import APIView
from .models import *
from .serializers import *



class OTPView(APIView):
    
    def get(self , request):
        serializer = RequersOTPResponseSerializer(data=request.query_params)
        if serializer.is_valid():
            data = serializer.validated_data
            print(1)
            try:
                otp = OTPRequest.objects.generate(data)
                print(2)
                return Response (data=RequersOTPResponseSerializer(otp).data)
                
            except Exception as e:
                print(3)
                return Response (status = status.HTTP_500_INTERNAL_SERVER_ERROR)     
        else : 
            print(4)
            return Response (status = status.HTTP_400_BAD_REQUEST , data=serializer.errors)
            
    
    def post(self , request): 
        pass
