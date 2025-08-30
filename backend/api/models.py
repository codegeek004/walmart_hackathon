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
    product_name = models.CharField(max_length=100)
    product_url = models.CharField(max_length=100)
    store = models.JSONField(default=list)
    reviews = models.JSONField(default=list)
    five_star = models.IntegerField(default=0)
    four_star = models.IntegerField(default=0)
    three_star = models.IntegerField(default=0)
    two_star = models.IntegerField(default=0)
    one_star = models.IntegerField(default=0)

    





