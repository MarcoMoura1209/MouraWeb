from django.test import TestCase
from core.forms import Form


class FormTest(TestCase):
    def test_form_com_todos_os_dados_validos(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
        }
        form = Form(data=dados)
        self.assertTrue(form.is_valid())

    def test_form_com_campo_nome_vazio(self):
        dados = {
            'nome': '',
            'email': 'email@gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)

    def test_form_com_campo_email_vazio(self):
        dados = {
            'nome': 'Nome',
            'email': '',
            'mensagem': 'Ola, tudo bem com voce?',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_form_com_campo_mensagem_vazio(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': '',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('mensagem', form.errors)

    def test_form_com_campo_mensagem_com_mais_de_1500_caracteres(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'x'*1501,
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('mensagem', form.errors)

    def test_form_com_campo_mensagem_com_exatamente_1500_caracteres(self):
        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'x'*1500,
        }
        form = Form(data=dados)
        self.assertTrue(form.is_valid())
        self.assertNotIn('mensagem', form.errors)

    def test_campo_email_com_formatacao_incorreta(self):
        dados = {
            'nome': 'Nome',
            'email': 'email-sem-arroba-gmail.com',
            'mensagem': 'Ola, tudo bem com voce?',
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_funcao_clean_mensagem_no_form(self):
        '''A funcao nao deve permitir mensagens com mais de 1500 caracteres'''

        dados = {
            'nome': 'Nome',
            'email': 'email@gmail.com',
            'mensagem': 'x' * 1501,
        }
        form = Form(data=dados)
        self.assertFalse(form.is_valid())
        self.assertIn('mensagem', form.errors)
        self.assertIn('máximo 1500', str(form.errors['mensagem']))
