from django.db import models

# Create your models here.
class Message(models.Model):
   sender=models.CharField(max_length=50)
   reciever = models.CharField(max_length=50)
   subject= models.CharField(max_length=100)
   content=models.TextField(blank=True)
   creation_date=models.TimeField(auto_now_add=True)
   read=models.BooleanField(default=False)

