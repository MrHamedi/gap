"""
WSGI config for gap project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

SETTINGS_PATH = os.environ.get("SETTINGS_PATH", "gap.settings.dev") 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', SETTINGS_PATH)

application = get_wsgi_application()
