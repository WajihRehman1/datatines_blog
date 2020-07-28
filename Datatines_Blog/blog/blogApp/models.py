from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.urls import reverse
from tinymce.models import HTMLField


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.user.username


class Catagory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    view_count = models.IntegerField(default=0)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    catagories = models.ManyToManyField(Catagory)
    featured = models.BooleanField()

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    def get_absolute_url(self):
        return reverse('blogApp:index')


class comment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    Post = models.ForeignKey(post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
