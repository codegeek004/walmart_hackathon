from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.db.models import Count, Q
from .serializers import *
from bson import ObjectId

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
        products_objects = products.find({}, {})
        ratings = []
        positive_count = 0
        for i in products_objects:
            ratings.append(i['store']['rating'])
            if i['reviews']['sentiment'] != 'negative':
                positive_count+=1
        
        tickets_qs = Tickets.objects.aggregate(
                active_tickets=Count('id', filter=Q(isResolved=False)),
                critical_issues=Count('id', filter=Q(category='critical'))
            )

        avg_rating = sum(ratings)/len(ratings)
        avg_rating = round(avg_rating, 2) 
     
        return Response({
                "total_feedbacks" : total_feedbacks,
                "positive_reviews" : positive_count,
                "active_tickets" : tickets_qs['active_tickets'],
                "critical_issues" : tickets_qs['critical_issues'],
                "average_rating" : avg_rating
            })

class Feedback(APIView):
    def get(self, request):
        products = list(db['api_product'].find({}, {'_id' : 0}))
        print(products)
        stores = []
        for i in products:
            print(i)
            stores.append(i['store'])
        print(stores)
        serializer = FeedbackSerializer(products, many=True)
        return Response({"products" : serializer.data, "stores" : stores})

    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Tickets(APIView):
    def get(self, request):
        try:
            tickets = list(db['api_tickets'].find({}, {'_id':0}))
            serializer = TicketSerializer(tickets, many=True)
            return Response({"tickets" : serializer.data})
        except Exception as e:
            return Response({"Error occurred" : e})        

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, ticket_id):
        try:
            ticket_id = ObjectId(ticket_id)
            document = db.api_ticket.find_one({"_id" : ticket_id})
            serializer = TicketSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Exception : {e}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






