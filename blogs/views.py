from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView
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

class detailPost(DetailView):
    model = Post
    template_name = 'blogs/detailPost.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class editPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blogs/editPost.html'
    fields = ['title', 'content']

    def form_valid(self, form):   #to update automatically the posted_date without giving the specific field form
        form.instance.date_posted = timezone.now()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.user != self.request.user:
            raise PermissionDenied("You are not allowed to edit this post.")
        return post

    def get_success_url(self):
        return reverse('detailPost', kwargs={'pk': self.object.pk})

class deletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blogs/post_confirm_delete.html'
    success_url = reverse_lazy('blog')

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        if post.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this post.")
        return post
