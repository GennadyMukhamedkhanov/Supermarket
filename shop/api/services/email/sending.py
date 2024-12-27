from django import forms
from django.core.mail import send_mail
from service_objects.services import Service
import random
from conf import settings


class EmailService(Service):
    email = forms.CharField(required=True, error_messages={'invalid': 'Введен неверный email'})


    def process(self):
        self.send_welcome_email()
        return self.code

    def send_welcome_email(self):
        subject = 'Пароль'
        self.code = str(random.randint(1000, 9999))
        message = self.code
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.cleaned_data['email']]

        send_mail(subject, message, email_from, recipient_list)