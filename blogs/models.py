from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('detailPost', kwargs={'pk': self.pk})
    def __str__(self):
        return f"{self.title} created by {self.user.username}"
