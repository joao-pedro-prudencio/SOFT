import unittest
from Sistema import Sistema
from UsuarioAdministrador import UsuarioAdministrador
from UsuarioCliente import UsuarioCliente

class Teste_UsuarioCliente(unittest.TestCase):

    # Verifica se os valores de Quantidade disponivel e quantidade comprada de um livro são alterados corretamente
    def test_comprar_livro(self):
        print("Teste 1- Verificando a compra do livro:")
        testeSistema = Sistema()
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro2", "Autor2", "Genero1", 0)
        UsuarioCliente.comprar_livro(testeSistema,"Livro1")

        # Verificando se o livro foi comprado com sucesso

        livro1 = testeSistema.lista_livros_total[0]
        # verificando se a quantidade comprada do primeiro livro criado é igual 1
        self.assertEqual(livro1.quantidade_comprada, 1)
        # verificando se a quantidade disponível do primeiro livro criado é igual 4
        self.assertEqual(livro1.quantidade_disponivel, 4)

    # Verifica se o primeiro e o terceiro livros da lista de livros compõem a lista de livros comprados
    def test_listar_livros_comprados(self):
        print("\nTeste 2- Verificando se os livros comprados vão para a lista de comprados:")
        testeSistema = Sistema()
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro2", "Autor2", "Genero2", 2)
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro3", "Autor3", "Genero3", 4)
        UsuarioCliente.comprar_livro(testeSistema, "Livro1")
        UsuarioCliente.comprar_livro(testeSistema, "Livro3")

        # Obtendo a lista de livros comprados
        livros_comprados = UsuarioCliente.listar_livros_comprados(testeSistema)

        livro1 = testeSistema.lista_livros_total[0]
        livro3 = testeSistema.lista_livros_total[2]
        listaLivrosCompradosTest = [livro1, livro3]

        # Verificando se a lista de livros comprados retornada pelo método listar_livros_comprados() é igual a lista criada manualmente
        # que insere os dois livros que escolhemos comprar: livros 1 e 3.
        self.assertEqual(livros_comprados, listaLivrosCompradosTest)

    # Verficando se o método de ver dados de um livro demonstra os dados corretos
    def test_ver_dados_livro(self):
        print("\nTeste 3- Verificando se os dados dos livros aparecem corretamente:")
        testeSistema = Sistema()
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)

        dadosLivro = UsuarioCliente.ver_dados_livro(testeSistema, "Livro1")

        dadosLivroTeste = ["Livro1", "Autor1", "Genero1"]

        self.assertEqual(dadosLivro, dadosLivroTeste)

if __name__ == "__main__":
    unittest.main()
