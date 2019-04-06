"""
WSGI config for Sentimental_Analysis_of_Trending_Topics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sentimental_Analysis_of_Trending_Topics.settings')

application = get_wsgi_application()
