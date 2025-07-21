from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField, ObjectIdField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(models.Model):
    id = ObjectIdAutoField(primary_key=True)    
    role = models.CharField(max_length=10, default='store_admin')
    contact = models.IntegerField(max_length=12)

class Store(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    location = models.CharField(max_length=100, default='Indore')
    revenue = models.FloatField(max_length=150, null=True)
    customers = models.IntegerField(max_length=100, null=True)
    employees = models.IntegerField(max_length=100)
    rating = models.FloatField(default=5)

class Tickets(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    category = models.CharField(max_length=100)
    isResolved = models.CharField(max_length=10)
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




