from django.urls import path
from account import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
	# eventually, want the index to be the home feed and redirect to the register page if the person isn't logged in
	path('', account_views.account_login, name='index'),

	path('register/', account_views.register, name='acc_register'),
	path('login/', account_views.account_login, name='acc_login'),
	path('logout/', auth_views.logout, { 'template_name': 'account/logout.html' }, name='acc_logout'),

	path('home/', account_views.home, name='home'),
]
