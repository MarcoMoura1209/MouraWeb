from django.urls import reverse, resolve
from django.test import TestCase, Client
from core.models import Cliente
from core import views


class ViwesHomeTest(TestCase):
    def setUp(self):
        self.client = Client()
        return super().setUp()

    def test_view_core_home_retorna_status_code_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_funcao_da_view_home_esta_correta(self):
        view = resolve(reverse('core:home'))
        self.assertIs(view.func, views.home)

    def test_view_home_retorna_template_correto(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/pages/home.html')

    def test_home_view_tem_form_no_contexto(self):
        response = self.client.get('/')
        self.assertIn('form', response.context)

    def test_metodo_post_com_formulario_valido_salva_corretamente(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
            'fax_number': '',
        }
        response = self.client.post('/', dados)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cliente.objects.count(), 1)

    def test_metodo_post_no_formulario_redireciona_corretamente(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
            'fax_number': '',
        }
        response = self.client.post('/', dados)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_metodo_post_no_formulario_com_honeypot_preenchido(self):
        '''Se honeypot for preenchido o post deve ser rejeitado!'''
   
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
            'fax_number': 'honeypotm preenchido',
        }
        response = self.client.post('/', dados)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Cliente.objects.count(), 0)

    def test_post_invalido_retorna_formulario_com_erros(self):
        dados = {
            'nome': '',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
            'fax_number': '',
        }
        response = self.client.post('/', dados)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertIn('nome', response.context['form'].errors)
