from django.shortcuts import render
import requests

home_page_url = 'http://127.0.0.1:8080/api/'
def home_page_view(request):
	response = requests.get(home_page_url).json()
	return render(request, 'home.html', response)

dashboard_url = 'http://127.0.0.1:8080/api/dashboard/'
def dashboard_view(request):
	response = requests.get(dashboard_url).json()
	print(response)
	return render(request, 'dashboard.html', response)