from django.core.mail import send_mail
from django.conf import settings


def sendmail(to, message):
    send_mail(f"Django mail about BLOG {message}",
              f"INFO:{message}",
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=False)
