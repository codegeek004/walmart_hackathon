from django.urls import path
from .views import *
urlpatterns = [
        path('', index_view, name='index_view'),
        path('dashboard/', Dashboard.as_view(), name='dashboard'),
        ]
