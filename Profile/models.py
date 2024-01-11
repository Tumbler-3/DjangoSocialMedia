from django.db import models
from User.models import CustomUser


class PostModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    text = models.TextField()
    pic = models.ImageField(upload_to='pictures', blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    updated = models.BooleanField(default=False)
    liked = models.ManyToManyField(CustomUser, related_name='liked_by',blank=True)
    responsed = models.ManyToManyField('self', blank=True)
    reposted = models.ManyToManyField(CustomUser, related_name='reposted_by',blank=True)
    saved = models.ManyToManyField(CustomUser, related_name='caved_by',blank=True)
    quoted = models.ManyToManyField('self', blank=True)

    @property
    def likes(self):
        return self.liked.all().count()
    
    @property
    def reposts(self):
        return self.reposted.all().count()

    @property
    def responses(self):
        return self.responsed.all().count()
    
    @property
    def saves(self):
        return self.saved.all().count()
    
    @property
    def quotes(self):
        return self.quoted.all().count()
    
    def __str__(self):
        return f'{self.author.username} {self.date}' 
    
    
class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.post.author.username} {self.post.date}' 
    