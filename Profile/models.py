from django.db import models
from User.models import CustomUser


class PostModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    text = models.TextField()
    pic = models.ImageField(upload_to='media/pictures', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)
    liked = models.ManyToManyField(CustomUser, related_name='liked_by',blank=True)
    responsed = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    @property
    def likes(self):
        return self.liked.all().count()

    @property
    def responses(self):
        return self.responsed.all().count()
    
    def __str__(self):
        return f'{self.author.username} {self.date}' 
