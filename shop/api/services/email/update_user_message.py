from django import forms
from django.core.mail import send_mail
from service_objects.services import Service
import random
from conf import settings


class UpdateUserMessageEmailService(Service):
    email = forms.CharField(required=True, error_messages={'invalid': 'Введен неверный email'})

    def process(self):
        self.send_message_email()
        return True

    def send_message_email(self):
        subject = 'Данные изменены'
        message = self.cleaned_data['email'] + '- Ваша почта'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.cleaned_data['email']]

        send_mail(subject, message, email_from, recipient_list)
