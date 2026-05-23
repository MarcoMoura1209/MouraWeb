from django.test import TestCase, override_settings, Client
from django.urls import reverse


class RateLimitTest(TestCase):

    @override_settings(RATELIMIT_ENABLE=True)
    def test_rate_limit_de_10_por_hora(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, gostaria de conversar com voces',
            'fax_number': '',
        }
        for _ in range(10):
            response = self.client.post('/', dados)
            self.assertEqual(response.status_code, 302)

        response = self.client.post('/', dados)
        self.assertEqual(response.status_code, 403)


class CsrfTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('core:home')
        self.csrf_client = Client(enforce_csrf_checks=True)

    def test_csrf_missing(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, gostaria de conversar com voces',
            'fax_number': '',
        }
        response = self.csrf_client.post(
            self.url, dados
        )
        self.assertEqual(response.status_code, 403)

    def test_csrf_present(self):
        get_response = self.csrf_client.get(self.url)
        csrf_token = get_response.cookies['csrftoken'].value

        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, gostaria de conversar com voces',
            'fax_number': '',
        }
        response = self.csrf_client.post(
            self.url, dados, HTTP_X_CSRFTOKEN=csrf_token
        )
        self.assertEqual(response.status_code, 302)
