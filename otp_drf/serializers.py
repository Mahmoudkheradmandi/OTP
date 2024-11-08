from rest_framework import serializers
from .models import OTPRequest
class RequestOTPSerializer(serializers.Serializer): 
    receiver = serializers.CharField(max_length=50 , allow_null=False)
    channel = serializers.ChoiceField(allow_null=False , choices = OTPRequest.OTPChannel.choices )
    
    
class RequersOTPResponseSerializer(serializers.ModelSerializer):
    
    class Meta: 
        
        model = OTPRequest
        fields = ['request_id']     