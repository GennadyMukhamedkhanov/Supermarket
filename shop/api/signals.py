from django.db.models.signals import post_save
from django.dispatch import receiver

from api.services.email.create_user_message import CreateUserMessageEmailService
from api.services.email.update_user_message import UpdateUserMessageEmailService
from db.models import User


@receiver(post_save, sender=User)
def create_author_profile(sender, instance, created, **kwargs):
    if created:
        CreateUserMessageEmailService.execute({'email': instance.email})


@receiver(post_save, sender=User)
def update_author_profile(sender, instance, created, **kwargs):
    if not created:
        UpdateUserMessageEmailService.execute({'email': instance.email})

