from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from django.views.static import serve

import account.views
import stream.views

urlpatterns = [
	# path('account/', include('account.urls')),
	# path('stream/', include('stream.urls')),

	re_path(r'^profile/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),

	path('login/', account.views.account_login, name='login'),
	path('register/', account.views.register, name='register'),
	path('logout/', auth_views.logout, { 'template_name': 'account/logout.html' }, name='logout'),

	path('profile/update/', account.views.update_profile, name='update_profile'),
	path('user/<cur_user>', account.views.profile, name='profile'),

	path('user/<username>/<post_id>/', stream.views.view_post, name='view_post'),

	path('stream/', stream.views.home, name='home'),
	path('stream/new_post/', stream.views.new_post, name='new_post'),
	path('stream/<post_id>/delete_post/', stream.views.delete_post, name='delete_post'),

	# access to admin tools
	path('admin/', admin.site.urls),
]
