from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

user = get_user_model()

@api_view(['GET'])
def index_view(request):
    if request.method == 'GET':
        return Response({"message" : "Welcome to Dashboard"})



