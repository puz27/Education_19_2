from django.core.mail import send_mail
from django.conf import settings


def sendmail(to, theme, message):
    send_mail(f"Django mail: {theme}",
              f"{message}",
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=False)
