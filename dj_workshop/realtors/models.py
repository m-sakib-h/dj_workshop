from django.db import models

# Create your models here.

class Realtor(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    desc=models.TextField(blank=True,verbose_name='description')
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    messsage=models.CharField(max_length=200)
    contact_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
