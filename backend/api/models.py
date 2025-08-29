from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField, ObjectIdField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(models.Model):
    id = ObjectIdAutoField(primary_key=True)    
    role = models.CharField(max_length=10, default='store_admin')
    contact = models.IntegerField()

class Tickets(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    category = models.CharField(max_length=100)
    isResolved = models.BooleanField()
    date = models.DateTimeField(default=timezone.now)
    store = models.JSONField(default=list)
    priority = models.CharField(max_length=50)


class Product(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    store_id = ObjectIdField(default="64e63c52f1a743f8bdcd91ab") 
    Title = models.CharField(max_length=120, blank=True)
    product_name = models.CharField(max_length=100)
    product_url = models.CharField(max_length=100)
    store = models.JSONField(default=list)
    reviews = models.JSONField(default=list)

    





