"""
Configuración de la URL para configurar el proyecto.

La lista `urlpatterns` enruta las URL a las vistas. Para más información, consulte:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Ejemplos:
Vistas de función
    1. Agregar una importación: desde :  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Vistas basadas en clases
    1. Agregar una importación:  from other_app.views import Home
    2. Agregar una URL a urlpatterns:  path('', Home.as_view(), name='home')
Incluyendo otra URLconf
    1. Importar la función include():para django.urls import include, path
    2. Agregar una URL a urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
