from django.db import models
from realtors.models import  Realtor

# Create your models here.

class Listing(models.Model):
    realtor=models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zip_code=models.CharField(max_length=150)
    desc=models.CharField(max_length=150, verbose_name='description')
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    garage=models.IntegerField()
    sqft=models.IntegerField()
    lot_size = models.DecimalField(decimal_places=2, max_digits=5)
    is_published = models.BooleanField()
    photo_main=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_5=models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_6=models.ImageField(upload_to='photos/%Y/%m/%d')
    list_date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



