from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.db.models import Count, Q

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
        
        positive_sentiment_qs = Product.objects.filter(sentiment="positive").count()
        tickets_qs = Tickets.objects.aggregate(
                active_tickets=Count('id', filter=Q(isResolved=False)),
                critical_issues=Count('id', filter=Q(category='critical'))
            )
        avg_rating = sum(ratings)/len(ratings)
        avg_rating = round(avg_rating, 2) 
     
        return Response({
                "Total Feedbacks" : total_feedbacks,
                "Positive Reviews" : positive_sentiment_qs,
                "Active Tickets" : tickets_qs['active_tickets'],
                "Critical Issues" : tickets_qs['critical_issues'],
                "Average Rating" : avg_rating
            })






