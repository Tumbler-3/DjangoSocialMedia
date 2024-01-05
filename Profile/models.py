from django.db import models


# Create your models here.
class PostModel(models.Model):
    text = models.TextField()
    pic = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField()