from django.test import TestCase
from core.models import Tecnologia


class TecnologiaModelTest(TestCase):
    def setUp(self):
        self.tecnologia = Tecnologia.objects.create(
            nome='Nome da tecnologia'
        )
        return super().setUp()

    def test_tecnologia_criada_com_sucesso(self):
        self.assertEqual(Tecnologia.objects.count(), 1)

    def test_salva_nome_da_tecnologia_corretamente(self):
        self.assertEqual(self.tecnologia.nome, 'Nome da tecnologia')

    def test_str_retorna_nome_da_tecnologia(self):
        self.assertEqual(str(self.tecnologia), 'Nome da tecnologia')

    def test_nome_invalido_com_mais_de_50_caracteres(self):
        nome_invalido = Tecnologia(
            nome='x'*51,
        )
        with self.assertRaises(Exception):
            nome_invalido.full_clean()
            nome_invalido.save()
