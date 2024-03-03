from concurrent.futures import process
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image= models.ImageField(upload_to='products', default='pix.jpg')
    def __str__(self):
        return self.name


class Processor(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.name 

    class Meta:
        db_table = 'processor'
        managed = True
        verbose_name = 'processor'
        verbose_name_plural = 'processors'

class Product(models.Model):
    name = models.CharField(max_length=50)
    fee = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.name 

    class Meta:
        db_table = 'sub'
        managed = True
        verbose_name = 'sub'
        verbose_name_plural = 'sub'
        
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=50)
    amount = models.CharField(max_length=50, blank=True, null=True)
    status  = models.BooleanField(default=False, null=True)
    date =models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.confirmation_code 

    class Meta:
        db_table = 'transaction'
        managed = True
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pending_transactions_id = models.CharField(max_length=50, null=True)
    paid_transactions_id = models.CharField(max_length=50, null=True)
    total_paid_amount = models.CharField(max_length=50, null=True)
    
    username = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question 

    class Meta:
        db_table = 'profile'
        managed = True
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'



