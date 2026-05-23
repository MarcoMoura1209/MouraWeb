from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models import Tecnologia, Skill, Cliente, Projeto
from io import BytesIO
from PIL import Image


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


class ProjetoModelTest(TestCase):
    def setUp(self):
        imagem = self._criar_imagem_teste()

        self.tecnologia = Tecnologia.objects.create(
            nome='Django',
        )

        self.projeto = Projeto.objects.create(
            titulo='Meu Projeto',
            descricao='Descrição do projeto',
            link_github='https://github.com/usuario/projeto',
            imagem=imagem,
            ordem=1,
        )
        self.projeto.tecnologias.add(self.tecnologia)
        return super().setUp()

    def _criar_imagem_teste(self):
        """Cria uma imagem fictícia para testes"""
        arquivo = BytesIO()
        imagem = Image.new('RGB', (100, 100), color='red')
        imagem.save(arquivo, 'JPEG')
        arquivo.seek(0)
        return SimpleUploadedFile(
            'test_image.jpg',
            arquivo.read(),
            content_type='image/jpeg'
        )

    def test_projeto_criado_com_sucesso(self):
        self.assertEqual(Projeto.objects.count(), 1)

    def test_str_retorna_titulo_do_projeto(self):
        self.assertEqual(str(self.projeto), 'Meu Projeto')

    def test_salva_titulo_corretamente(self):
        self.assertEqual(self.projeto.titulo, 'Meu Projeto')

    def test_titulo_invalido_com_mais_de_50_caracteres(self):
        titulo_invalido = Projeto(
            titulo='x' * 51,
            descricao='Descrição do projeto',
            link_github='https://github.com/usuario/projeto',
            imagem=self._criar_imagem_teste(),
            ordem=1,
        )
        with self.assertRaises(Exception):
            titulo_invalido.full_clean()
            titulo_invalido.save()

    def test_salva_descricao_corretamente(self):
        self.assertEqual(self.projeto.descricao, 'Descrição do projeto')

    def test_salva_link_github_corretamente(self):
        self.assertEqual(self.projeto.link_github, 'https://github.com/usuario/projeto')

    def test_link_github_invalido_sem_url_valida(self):
        link_invalido = Projeto(
            titulo='Projeto',
            descricao='Descrição',
            link_github='nao-e-uma-url-valida',
            imagem=self._criar_imagem_teste(),
            ordem=1,
        )
        with self.assertRaises(Exception):
            link_invalido.full_clean()
            link_invalido.save()

    def test_salva_ordem_corretamente(self):
        self.assertEqual(self.projeto.ordem, 1)

    def test_ordem_padrão_e_zero(self):
        imagem = self._criar_imagem_teste()
        projeto_sem_ordem = Projeto.objects.create(
            titulo='Projeto Sem Ordem',
            descricao='Descrição',
            link_github='https://github.com/usuario/projeto2',
            imagem=imagem,
        )
        self.assertEqual(projeto_sem_ordem.ordem, 0)

    def test_adiciona_tecnologia_ao_projeto(self):
        self.assertIn(self.tecnologia, self.projeto.tecnologias.all())

    def test_projeto_pode_ter_multiplas_tecnologias(self):
        tecnologia2 = Tecnologia.objects.create(nome='React')
        self.projeto.tecnologias.add(tecnologia2)
        self.assertEqual(self.projeto.tecnologias.count(), 2)

    def test_imagem_salva_corretamente(self):
        self.assertTrue(self.projeto.imagem)
        self.assertIn('test_image', self.projeto.imagem.name)
