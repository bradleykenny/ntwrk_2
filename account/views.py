from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm, UserForm, ProfileForm
from stream.models import Post

def index(request):
	return render(request, 'home.html')

def home(request):
	return render(request, 'account/home.html')

# TODO: make this per user, not just for the logged in user
def profile(request, cur_user):
	posts = Post.objects.all()
	cur_user_obj = User.objects.get(pk=cur_user)
	# cur_user_obj.profile.dp = 'dp/placeholder2.png'
	# cur_user_obj.save()
	return render(request, 'account/profile.html', { 'posts': posts, 'cur_user': cur_user_obj })


def account_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('home')
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		form = LoginForm()
	return render(request, 'account/login.html', { 'form': form })


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')
	else:
		form = RegistrationForm()
	return render(request, 'account/register.html', { 'form': form })


# TODO: IMPLEMENT @login and @transaction
# @transaction.atomic
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('../../profile/update')
        # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })


@login_required
def user_follow(request):
	return


def dp_img(request):
	return render(request, 'MEDIA/dp/')

def account_logout(request):
	logout(request)
	return render(request, 'account/logout.html')