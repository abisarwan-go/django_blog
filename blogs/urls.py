from django.urls import path

from . import views


urlpatterns = [
    path("", views.blog, name='blog'),
    path("submitPost/", views.submitPost, name='submitPost'),
    path("<int:pk>/", views.detailPost.as_view(), name='detailPost'),
    path("editPost/<int:pk>/", views.editPost.as_view(), name='editPost'),
    path("deletePost/<int:pk>/", views.deletePost.as_view(), name='deletePost'),
    ]


