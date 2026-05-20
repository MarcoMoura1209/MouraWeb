from django.test import TestCase
from core.models import Tecnologia, Skill, Cliente


class TecnologiaModelTest(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(
            nome='Nome da tecnologia',
        )
        return super().setUp()

    def test_tecnologia_criada_com_sucesso(self):
        self.assertEqual(Tecnologia.objects.count(), 1)

    def test_salva_nome_da_tecnologia_corretamente(self):
        self.assertEqual(self.tecnologia.nome, 'Nome da tecnologia')

    def test_str_retorna_nome_da_tecnologia(self):
        self.assertEqual(str(self.tecnologia), 'Nome da tecnologia')

    def test_nome_da_tecnologia_invalido_com_mais_de_50_caracteres(self):
        nome_invalido = Tecnologia(
            nome='x'*51,
        )
        with self.assertRaises(Exception):
            nome_invalido.full_clean()
            nome_invalido.save()


class SkillModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            nome='Nome da skill',
            porcentagem=100,
        )
        return super().setUp()

    def test_skill_criada_com_sucesso(self):
        self.assertEqual(Skill.objects.count(), 1)

    def test_salva_nome_da_skill_corretamente(self):
        self.assertEqual(self.skill.nome, 'Nome da skill')

    def test_str_retorna_nome_da_skill(self):
        self.assertEqual(str(self.skill), 'Nome da skill')

    def test_nome_da_skill_invalido_com_mais_de_50_caracteres(self):
        nome_invalido = Skill(
            nome='x'*51,
        )
        with self.assertRaises(Exception):
            nome_invalido.full_clean()
            nome_invalido.save()

    def test_salva_skill_porcentagem_corretamente(self):
        self.assertEqual(self.skill.porcentagem, 100)


class ClienteModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome='Nome',
            email='email@gmail.com',
            mensagem='Ola, tudo bem?',
        )
        return super().setUp()

    def test_cliente_criado_com_sucesso(self):
        self.assertEqual(Cliente.objects.count(), 1)

    def test_str_retorna_nome_do_cliente(self):
        self.assertEqual(str(self.cliente), 'Nome')

    def test_salva_nome_do_cliente_corretamente(self):
        self.assertEqual(self.cliente.nome, 'Nome')

    def test_nome_do_cliente_invalido_com_mais_de_30_caracteres(self):
        nome_invalido = Cliente(
            nome='x'*31,
            email='email@gmail.com',
            mensagem='Ola, tudo bem?',
        )
        with self.assertRaises(Exception):
            nome_invalido.full_clean()
            nome_invalido.save()

    def test_email_cliente_salvo_corretamente(self):
        self.assertEqual(self.cliente.email, 'email@gmail.com')

    def test_email_cliente_invalido_sem_arroba(self):
        email_invalid0 = Cliente(
            nome='Nome',
            email='email-gmail.com',
            mensagem='Ola, tudo bem?',
        )
        with self.assertRaises(Exception):
            email_invalid0.full_clean()
            email_invalid0.save()

    def test_email_cliente_com_formato_valido(self):
        email_invalid0 = Cliente(
            nome='Nome',
            email='email@gmail.com',
            mensagem='Ola, tudo bem?',
        )
        email_invalid0.full_clean()
        email_invalid0.save()

    def test_mensagem_cliente_invalida_com_mais_de_1500_caracteres(self):
        cliente_invalido = Cliente(
            nome='Nome',
            email='email@gmail.com',
            mensagem='x' * 1501,
        )
        with self.assertRaises(Exception):
            cliente_invalido.full_clean()
            cliente_invalido.save()

    def test_mensagem_cliente_valida(self):
        cliente_invalido = Cliente(
            nome='Nome',
            email='email@gmail.com',
            mensagem='x' * 1500,
        )
        cliente_invalido.full_clean()
        cliente_invalido.save()
