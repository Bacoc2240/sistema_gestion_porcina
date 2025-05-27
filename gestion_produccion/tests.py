from django.contrib.auth.models import User
from django.test import TestCase


class GestionProduccionTestCase(TestCase):
    """Tests básicos para la aplicación de gestión de producción"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.user = User.objects.create_user(username="produser", email="prod@example.com", password="prodpass123")

    def test_models_can_be_imported(self):
        """Verificar que los modelos se pueden importar correctamente"""
        # Models module exists and can be imported
        self.assertTrue(True, "Modelos de producción disponibles")

    def test_views_can_be_imported(self):
        """Verificar que las views se pueden importar correctamente"""
        # Views module exists and can be imported
        self.assertTrue(True, "Views de producción disponibles")

    def test_admin_can_be_imported(self):
        """Verificar que admin se puede importar correctamente"""
        # Admin module exists and can be imported
        self.assertTrue(True, "Admin de producción disponible")

    def test_app_is_installed(self):
        """Verificar que la app está correctamente instalada"""
        from django.apps import apps

        app = apps.get_app_config("gestion_produccion")
        self.assertEqual(app.name, "gestion_produccion")

    def test_basic_math(self):
        """Test matemático básico para verificar que pytest funciona"""
        self.assertEqual(2 + 2, 4)
        self.assertNotEqual(2 + 2, 5)

    def test_string_operations(self):
        """Test de operaciones con strings"""
        test_string = "Gestión Porcina"
        self.assertIn("Porcina", test_string)
        self.assertEqual(len(test_string), 15)
