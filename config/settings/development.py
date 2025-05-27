"""
Configuración para desarrollo local
"""

from .base import *

# Debug habilitado en desarrollo
DEBUG = True

# Hosts permitidos en desarrollo
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Base de datos para desarrollo (tu configuración actual)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME", "gestion_porcina"),
        "USER": os.getenv("DATABASE_USER", "porcina_admin"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD", "password_seguro"),
        "HOST": os.getenv("DATABASE_HOST", "localhost"),
        "PORT": os.getenv("DATABASE_PORT", "5432"),
    }
}

# Configuración de logging para desarrollo
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "gestion_reproductiva": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "gestion_produccion": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "administracion": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# CORS para desarrollo (si usas frontend separado)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React
    "http://localhost:8080",  # Vue
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
]

# Email backend para desarrollo (simula envío de emails)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
