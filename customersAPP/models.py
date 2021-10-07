from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Costumer(models.Model):
     name = models.CharField(max_length = 50, null=False)
     surname = models.CharField(max_length = 50, null=False)
     photo = models.ImageField(null=True, upload_to='customersAPP')
     lastupdateuser= models.ForeignKey(User,on_delete=models.SET_NULL,related_name="lastupdateuser",null=True)
     creatoruser = models.ForeignKey(User,on_delete=models.SET_NULL,related_name="creatoruser",null=True)
     def __str__(self):
          return '{0},{1}'.format(self.surname,self.name)