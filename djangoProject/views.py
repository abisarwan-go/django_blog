from django.http import Http404
from django.shortcuts import render

from blogs.models import Post


def home(request):
    posts = Post.objects.all()
    for post in posts:
        post.content = post.content[:100] + '...' if len(post.content) > 100 else post.content
    return render(request, "home.html", {"posts": posts})


def custom_forbidden_view(request, exception=None):
    message = str(exception) if exception else "You do not have permission to access this resource."
    response = render(request, '403.html', {"message": message})
    response.status_code = 403
    return response