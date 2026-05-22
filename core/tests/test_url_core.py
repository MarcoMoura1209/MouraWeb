from django.test import TestCase
from django.urls import reverse


class CoreUrlTest(TestCase):

    def test_url_home_resolve_corretamente(self):
        home_url = reverse('core:home')
        self.assertEqual(home_url, '/')

    def test_url_admin_resolve_corretamente(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 302])
