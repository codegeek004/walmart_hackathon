from rest_framework import serializers
from .models import *
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewSerializer(serializers.Serializer):
	reviewer_name = serializers.CharField(max_length=100)
	review = serializers.CharField()
	review_date = serializers.DateTimeField(default=timezone.now)
	sentiment = serializers.CharField(max_length=50, default="positive")
	

class StoreSerializer(serializers.Serializer):
	location = serializers.CharField(max_length=100, default='Palasia, Indore')
	revenue = serializers.FloatField()
	customers = serializers.IntegerField()
	employees = serializers.IntegerField()
	rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

class FeedbackSerializer(serializers.ModelSerializer):
	id = serializers.CharField(read_only=True)
	store = StoreSerializer()
	reviews = ReviewSerializer()

	class Meta:
		model = Product
		fields = "__all__"

	def create(self, validated_data):
		return Product.objects.create(**validated_data)



	










