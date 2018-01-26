from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

import account.views
import stream.views

urlpatterns = [
	# sub-parts to app
	# path('account/', include('account.urls')),
	# path('stream/', include('stream.urls')),

	# THIS IS HOW TO DO THE APP
	path('login/', account.views.account_login, name='login'),
	path('register/', account.views.register, name='register'),
	path('logout/', auth_views.logout, { 'template_name': 'account/logout.html' }, name='logout'),

	path('stream/', stream.views.home, name='home'),
	path('stream/new_post/', stream.views.new_post, name='new_post'),
	path('stream/<post_id>/delete_post/', stream.views.delete_post, name='delete_post'),
	path('stream/<post_id>/view_post/', stream.views.view_post, name='view_post'),

	# access to admin tools
	path('admin/', admin.site.urls),
]
