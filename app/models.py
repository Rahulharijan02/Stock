
from asyncio.windows_events import NULL
from email.policy import default
from enum import unique
from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class query(models.Model):
 username = models.CharField(max_length=100)   
 stockname = models.CharField(max_length=100)
 query = models.TextField(max_length= 400)

class stock(models.Model):
 stockname = models.CharField(max_length=100)   
 image = models.ImageField(upload_to="myimage")
 description = models.TextField(max_length= 400)
 dslug = AutoSlugField(populate_from='description',unique= True,null=True, default=None)

 

 
 
