import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class OTPManger(models.Manager): 
    def generate(self , data):
        otp = self.model(channel=data['channel'] , receiver=data['receiver'])
        otp.save(using=self._db)
        return otp

class OTPRequest(models.Model): 
    class OTPChannel(models.TextChoices): 
        PHONE = 'phone'
        EMAIL = 'E-Mail'

    request_id = models.UUIDField(primary_key=True , editable=False , default=uuid.uuid4 )
    channel = models.CharField(choices=OTPChannel.choices , max_length=10 , default =OTPChannel.PHONE)
    receiver = models.CharField(max_length=50)
    password = models.CharField(max_length=4)
    created = models.DateTimeField(auto_now_add=True , editable=False)
    
    objects = OTPManger()