from .models import Author
from user.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(pre_save, sender = Author)
def update_request_status(sender, instance, **kwargs):
    user = User.objects.get(id = instance.user_id)
    if instance.is_approved:
        instance.request_status = True
        user.is_author = True
        user.save()
        
    if instance.is_blocked:
        user.is_author = False
        user.save()
        
@receiver(post_save, sender = User)
def update_author_status(sender, instance, **kwargs):
    
    try:
        author = Author.objects.get(user_id = instance.id)
    except:
        author = None
        
    if author:
        if instance.is_superuser:
            if not author.is_approved:
                author.is_approved = True
                author.save()
    # else:
    #     if instance.is_superuser:
    #         Author.objects.create(user_id = instance, is_approved = True)
    #         Author.save()