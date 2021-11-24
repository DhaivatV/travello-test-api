from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class Destination(models.Model):
    name= models.CharField(max_length=100)
    descr= models.TextField()
    image= models.ImageField(upload_to= 'pics')
    price= models.IntegerField()
    offers= models.BooleanField(default=False)
    rating= models.IntegerField()
