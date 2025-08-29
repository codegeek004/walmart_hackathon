from rest_framework import serializers
from .models import *
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewSerializer(serializers.Serializer):
	reviewer_name = serializers.CharField(max_length=100)
	review = serializers.CharField()
	review_date = serializers.DateTimeField(default=timezone.now)
	five_star = serializers.IntegerField()
	four_star = serializers.IntegerField()
	three_star = serializers.IntegerField()
	two_star = serializers.IntegerField()
	one_star = serializers.IntegerField()

class StoreSerializer(serializers.Serializer):
	location = serializers.CharField(max_length=100, default='Palasia, Indore')
	revenue = serializers.FloatField()
	customers = serializers.IntegerField()
	employees = serializers.IntegerField()
	rating = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

class FeedbackSerializer(serializers.ModelSerializer):
	store = StoreSerializer()
	reviews = ReviewSerializer(many=True)

	class Meta:
		model = Product
		fields = "__all__"

	


	










