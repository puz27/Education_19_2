from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

import config.settings
from catalog.models import Category

def sendmail(to, theme, message):
    send_mail(f"Django mail: {theme}",
              f"{message}",
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=False)


def get_categories():
    """Return categories with cash"""
    if config.settings.CACHE_ENABLED:
        key = 'categories'
        cache_data = cache.get(key)
        if cache_data is None:
            cache_data = Category.objects.all()
            cache.set(key, cache_data)
    else:
        cache_data = Category.objects.all()
    return cache_data



