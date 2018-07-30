from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Post

def home(request):
	posts = Post.objects.all()
	users = User.objects.all()
	return render(request, 'stream/home.html', {'posts': posts, 'users': users})

def new_post(request):
	if request.method == 'POST':
		content = request.POST['content']
		user = request.user
		post = Post.objects.create(content=content, posted_by=user)

		return redirect('home')

	return render(request, 'stream/new_post.html')

def edit_post(request):
	return

def delete_post(request, post_id):
	post = Post.objects.get(id=post_id)
	post_user = post.posted_by
	current_user = request.user

	if post.posted_by == request.user:
		post.delete()
	return render(request, 'stream/delete_post.html', {'post': post, 'current_user': current_user, 'post_user': post_user })

def view_post(request, username, post_id):
	# NOTE: implement in template too
	post = Post.objects.get(id=post_id)
	return render(request, 'stream/view_post.html', {'post':post})
