from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField, ObjectIdField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(models.Model):
    id = ObjectIdAutoField(primary_key=True)    
    role = models.CharField(max_length=10, default='store_admin')
    contact = models.IntegerField()

class Store(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    location = models.CharField(max_length=100, default='Indore')
    revenue = models.FloatField(null=True)
    customers = models.IntegerField(null=True)
    employees = models.IntegerField()
    rating = models.FloatField(default=5)

class Tickets(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    category = models.CharField(max_length=100)
    isResolved = models.BooleanField(max_length=10)
    date = models.DateTimeField(default=timezone.now())
    priority = models.CharField(max_length=50)

class Product(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    store_id = ObjectIdField(default="64e63c52f1a743f8bdcd91ab") 
    Title = models.CharField(max_length=120, blank=True)
    product_name = models.CharField(max_length=100)
    product_url = models.CharField(max_length=100)
    sentiment = models.CharField(max_length=100)
    review = models.CharField(max_length=150)
    reviewer_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now())




