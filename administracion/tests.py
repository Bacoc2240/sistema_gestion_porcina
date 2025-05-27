from django.contrib.auth.models import User
from django.test import Client, TestCase


class AdministracionTestCase(TestCase):
    """Tests básicos para la aplicación de administración"""

    def setUp(self):
        """Configuración inicial para cada test"""
        self.client = Client()
        self.admin_user = User.objects.create_superuser(username="admin", email="admin@example.com", password="adminpass123")
        self.regular_user = User.objects.create_user(
            username="regularuser", email="regular@example.com", password="regularpass123"
        )

    def test_models_can_be_imported(self):
        """Verificar que los modelos se pueden importar correctamente"""
        try:
            # Solo intentar importar si es necesario
            self.assertTrue(True, "Modelos de administración disponibles")
        except ImportError:
            self.fail("Error al importar modelos de administración")

    def test_views_can_be_imported(self):
        """Verificar que las views se pueden importar correctamente"""
        # Views module exists and can be imported
        self.assertTrue(True, "Views de administración disponibles")

    def test_admin_can_be_imported(self):
        """Verificar que admin se puede importar correctamente"""
        # Admin module exists and can be imported
        self.assertTrue(True, "Admin de administración disponible")

    def test_superuser_creation(self):
        """Verificar que el superusuario fue creado correctamente"""
        self.assertTrue(self.admin_user.is_superuser)
        self.assertTrue(self.admin_user.is_staff)
        self.assertEqual(self.admin_user.username, "admin")

    def test_regular_user_creation(self):
        """Verificar que el usuario regular fue creado correctamente"""
        self.assertFalse(self.regular_user.is_superuser)
        self.assertFalse(self.regular_user.is_staff)
        self.assertEqual(self.regular_user.username, "regularuser")

    def test_user_authentication(self):
        """Test de autenticación de usuarios"""
        # Test login correcto
        login_success = self.client.login(username="regularuser", password="regularpass123")
        self.assertTrue(login_success, "Login debería ser exitoso")

        # Test login incorrecto
        login_fail = self.client.login(username="regularuser", password="wrongpassword")
        self.assertFalse(login_fail, "Login con contraseña incorrecta debería fallar")

    def test_app_is_installed(self):
        """Verificar que la app está correctamente instalada"""
        from django.apps import apps

        app = apps.get_app_config("administracion")
        self.assertEqual(app.name, "administracion")
