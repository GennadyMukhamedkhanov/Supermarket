import time

from django.db.models.signals import post_save
from django.dispatch import receiver

from db.models import User
from .tasks import task_create_user_message, task_update_user_message


@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        task_create_user_message.delay(instance.email)



@receiver(post_save, sender=User)
def update_author_profile(sender, instance, created, **kwargs):
    if not created:
        task_update_user_message.delay(instance.email)


