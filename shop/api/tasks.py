import time

from celery import shared_task

from api.services.email.create_user_message import CreateUserMessageEmailService
from api.services.email.update_user_message import UpdateUserMessageEmailService


@shared_task
def task_create_user_message(email):
    CreateUserMessageEmailService.execute({'email': email})




@shared_task
def task_update_user_message(email):
    UpdateUserMessageEmailService.execute({'email': email})
