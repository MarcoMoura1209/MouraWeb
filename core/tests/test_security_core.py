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
