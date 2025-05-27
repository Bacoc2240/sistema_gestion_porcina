"""
Configuración de ASGI para el proyecto de configuración.

Expone el objeto invocable de ASGI como una variable a nivel de módulo denominada ``application``.

Para más información sobre este archivo, consulte
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_asgi_application()
