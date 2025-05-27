"""
Configuración automática de settings basada en la variable DJANGO_SETTINGS_MODULE
"""

import os

# Determinar qué configuración usar
ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT", "development")

if ENVIRONMENT == "production":
    from .production import *
elif ENVIRONMENT == "test":
    from .test import *
else:
    from .development import *
