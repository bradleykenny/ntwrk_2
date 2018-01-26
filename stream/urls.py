from django.urls import path
from . import views

urlpatterns = [
	# eventually, want the index to be the home feed and redirect to the register page if the person isn't logged in
	path('', views.home, name='str_home'),
]
