from django.shortcuts import render
import requests

dashboard_url = 'http://127.0.0.1:8000/dashboard'
def dashboard_view(request):
	return render(request, 'dashboard.html')
