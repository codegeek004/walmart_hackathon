from django.urls import path
from .views import *
urlpatterns = [
        path('', index_view, name='index_view'),
        path('dashboard/', Dashboard.as_view(), name='dashboard'),
        path('feedback/', Feedback.as_view(), name='feedback'),
        path('tickets/', Tickets.as_view(), name='tickets'),
        path('tickets/<str:ticket_id>/', Tickets.as_view(), name='ticket_status_update')
        ]
