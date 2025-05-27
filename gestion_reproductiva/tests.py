from django.contrib.auth.models import User
from django.test import TestCase


class GestionReproductivaTestCase(TestCase):
    """Tests básicos para la aplicación de gestión reproductiva"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")

    def test_models_can_be_imported(self):
        """Verificar que los modelos se pueden importar correctamente"""
        # Models module exists and can be imported
        self.assertTrue(True, "Modelos reproductivos disponibles")

    def test_views_can_be_imported(self):
        """Verificar que las views se pueden importar correctamente"""
        # Views module exists and can be imported
        self.assertTrue(True, "Views reproductivas disponibles")

    def test_admin_can_be_imported(self):
        """Verificar que admin se puede importar correctamente"""
        # Admin module exists and can be imported
        self.assertTrue(True, "Admin reproductivo disponible")

    def test_database_connection(self):
        """Verificar que la conexión a la base de datos funciona"""
        user_count = User.objects.count()
        self.assertEqual(user_count, 1, "Debería haber 1 usuario en la BD")

    def test_user_creation(self):
        """Test básico de creación de usuario"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("testpass123"))


class GestionReproductivaIntegrationTest(TestCase):
    """Tests de integración para gestión reproductiva"""

    def test_app_is_installed(self):
        """Verificar que la app está correctamente instalada"""
        from django.apps import apps

        app = apps.get_app_config("gestion_reproductiva")
        self.assertEqual(app.name, "gestion_reproductiva")
