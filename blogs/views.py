from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.
@login_required
def blog(request):
    form = PostForm(request.POST)
    posts = Post.objects.filter(user=request.user)
    for post in posts:
        post.content = post.content[:100] + '...' if len(post.content) > 100 else post.content
    return render(request, "blogs/blogs.html", {"form": form, "posts": posts})

def submitPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Create a model instance but don't save to the database yet
            post.user = request.user        # Set the user field
            post.save()                     # Now save the instance to the database
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blogs/submitPost.html', {'form': form})



