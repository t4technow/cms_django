from django.db import models
from user.models import User
# Create your models here.

class Author(models.Model):

    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 30)
    personal_website = models.CharField(max_length=200, null=True, blank=True)
    sample_link = models.TextField(null = True, blank=True)
    
    # if request is approved by admin
    is_approved = models.BooleanField(default = False)
    is_blocked = models.BooleanField(default=False)
    
    # if request is opened by the admin
    request_status = models.BooleanField(default=False)
    request_date = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name
