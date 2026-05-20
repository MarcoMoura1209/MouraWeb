import pytest
from django.core.management import call_command
from django.test import TestCase, override_settings
from io import StringIO
import sys


class ServerStartupTest(TestCase):
    """Testa se o servidor consegue iniciar sem erros."""

    def test_server_boots_without_errors(self):
        """
        Simula 'python manage.py runserver' captando erros de inicialização.
        Se houver erro de settings, importação ou banco, este teste falha.
        """
        out = StringIO()
        err = StringIO()

        try:
            # Tenta rodar check (equivalente ao que Django faz ao iniciar)
            call_command('check', stdout=out, stderr=err)
        except Exception as e:
            self.fail(f"Django check falhou ao iniciar: {str(e)}")

        output = out.getvalue()
        errors = err.getvalue()

        # Se houver erros, falha o teste
        self.assertFalse(errors, f"Erros durante inicialização: {errors}")
        self.assertIn("System check identified no issues", output)

    @override_settings(DEBUG=True)
    def test_django_settings_load_correctly(self):
        """
        Valida que as settings carregam sem problemas.
        """
        from django.conf import settings

        # Se chegou aqui, settings carregou
        self.assertTrue(hasattr(settings, 'CONTENT_SECURITY_POLICY_REPORT_ONLY'))
        self.assertTrue(hasattr(settings, 'SECRET_KEY'))
        self.assertIsNotNone(settings.SECRET_KEY)

    def test_database_connection(self):
        """
        Testa se consegue se conectar ao banco.
        """
        from django.db import connection

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except Exception as e:
            self.fail(f"Falha ao conectar no banco de dados: {str(e)}")
