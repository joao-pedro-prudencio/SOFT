import unittest
from Sistema import Sistema
from UsuarioAdministrador import UsuarioAdministrador
from Livro import Livro

class Teste_UsuarioAdministrador(unittest.TestCase):

    # Testando se o novo livro criado com o método inserir_novo_livro está na lista_livros_total do sistema
    def test_inserir_novo_livro(self):
        print("\nTeste 1- Verificando se o livro está na lista de livros total:")
        testeSistema = Sistema()

        # Inserção bem-sucedida
        livro1 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)

        # Verifica se o livro está na lista de livros total
        self.assertIn(livro1, testeSistema.lista_livros_total)

    # Testando se ao tentar criar um livro com o mesmo título de um já criado com o método inserir_novo_livro() 
    # ele não será criado

    def test_inserir_novo_livro_livro_existente(self):
        print("\nTeste 2- Verificando se dá de inserir um livro com o mesmo título:")
        testeSistema = Sistema()

        # Inserção inicial
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)

        # Tenta inserir um livro com o mesmo título
        livro2 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor2", "Genero2", 2)

        # Verifica se o método retorna None
        self.assertIsNone(livro2)

    # Testando se ao tentar criar um livro com um valor não numérico no campo "quantidade" com o método inserir_novo_livro() 
    # ele não será criado

    def test_inserir_novo_livro_quantidade_invalida(self):
        print("\nTeste 3- Verificando se dá de inserir um livro com quantidade não numérica:")
        testeSistema = Sistema()

        # Tenta inserir um livro com quantidade não numérica
        livro3 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro3", "Autor3", "Genero3", "invalida")

        # Verifica se o método retorna None
        self.assertIsNone(livro3)

    # Testando se ao criar um livro com o método inserir_novo_livro() ele vai para a lista_livros_total do sistema

    def test_inserir_tres_livros(self):
        print("\nTeste 4: Verificando se os livros inseridos vão para a lista_livros_total")
        testeSistema = Sistema()

        # Inserção de três livros
        livro1 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)
        livro2 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro2", "Autor2", "Genero2", 3)
        livro3 = UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro3", "Autor3", "Genero3", 8)

        # Verifica se os livros estão na lista de livros total
        self.assertIn(livro1, testeSistema.lista_livros_total)
        self.assertIn(livro2, testeSistema.lista_livros_total)
        self.assertIn(livro3, testeSistema.lista_livros_total)

    # Testando se o atributo quantidade disponivel de um livro realmente aumenta ao executar 
    # o método aumentar_quantidade_estoque

    def test_aumentar_quantidade_estoque_sucesso(self):
        print("\nTeste 5:")
        testeSistema = Sistema()
        UsuarioAdministrador.inserir_novo_livro(testeSistema, "Livro1", "Autor1", "Genero1", 5)
        UsuarioAdministrador.aumentar_quantidade_estoque(testeSistema, "Livro1", 3)
        livro1 = testeSistema.lista_livros_total[0]
        self.assertEqual(livro1.quantidade_disponivel, 8)

if __name__ == "__main__":
    unittest.main()
