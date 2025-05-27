"""
Configuración específica para tests
"""

from .base import *

# Debug deshabilitado en tests
DEBUG = False

# Base de datos en memoria para tests más rápidos
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Password hasher más rápido para tests
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]


# Deshabilitar migraciones para tests más rápidos
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Email backend para tests
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Media files en directorio temporal
MEDIA_ROOT = "/tmp/test_media"

# Cache en memoria para tests
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Deshabilitar logging durante tests
LOGGING_CONFIG = None

# Secret key fija para tests
SECRET_KEY = "test-secret-key-not-for-production"
