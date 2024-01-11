from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(blank=True,max_length=15,null=True)
    avatar = models.ImageField(upload_to='avatar')
    email = models.EmailField(blank=True,null=True)
    name = models.CharField(blank=True,null=False, max_length = 50)
    username = models.CharField(blank=True,null=False, max_length = 50, unique=True)
    password = models.CharField(blank=True,null=True, max_length = 30)
    first_name = None
    last_name = None
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name","email","password"]
