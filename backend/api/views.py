from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from pymongo import MongoClient

try:
    client = MongoClient('mongodb://root:root@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.3')
    db = client['walmart']
except Exception as e:
    print(f'Exception is {e}')

user = get_user_model()

@api_view(['GET'])
def index_view(request):
    if request.method == 'GET':
        return Response({"message" : "Welcome to Dashboard"})

class Dashboard(APIView):
    def get(self, request, *args, **kwargs):
        total_feedbacks = Product.objects.count()
        
        products = db['api_product']
        products_objects = products.find({}, {"_id":0, "Rating":1})
        ratings = []
        for i in products_objects:
            rating = i["Rating"]
            ratings.append(int(rating))
        
        sentiment_qs = Product.objects.filter(sentiment="positive").count()
        critical_issues = Tickets.objects.filter(category='critical').count()
        avg_rating = sum(ratings)/len(ratings)
     
        return Response({
                "Total Feedbacks" : total_feedbacks,
                "Sentiments" : sentiment_qs,
                "Critical Issues" : critical_issues,
                "Average Rating" : avg_rating
            })






