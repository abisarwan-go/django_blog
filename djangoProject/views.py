from django.shortcuts import render

from blogs.models import Post


def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.content = post.content[:100] + '...' if len(post.content) > 100 else post.content
    return render(request, "home.html", {"posts": posts})


