from django.db import models
# Create your models here.


class PageVisit(models.Model):
    user_id = models.CharField(max_length=100, default=0)
    session_key = models.CharField(max_length=350)
    url = models.CharField(max_length=250)
    visited_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:

        verbose_name = 'PageVisit'
        verbose_name_plural = 'PageVisit'

    def __str__(self):
        return self.url