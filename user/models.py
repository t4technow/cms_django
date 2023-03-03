from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='user/profile_pic')
    following_authors = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    is_author = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return self.username
