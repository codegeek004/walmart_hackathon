from django.contrib.auth.models import AbstractUser
from djongo import models
from django.utils import timezone

class CustomUser(AbstractUser):
	ROLE_CHOICES = [
		('admin','Central Admin'),
		('manager', 'Store Admin')
	]
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
	contact = models.IntegerField(max_length=12)
	def __str__(self):
		return self.username


class Product(models.Model):
    Name = models.CharField(max_length=50)
    url = models.CharField(max_length=300)
    sentiment = models.CharField(max_length=50)

    def review_count(self):
        return self.reviews.count()

    def __str__(self):
        return self.Name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=50)
    review = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=0)

