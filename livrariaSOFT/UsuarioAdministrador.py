from Livro import Livro

class UsuarioAdministrador:
    @staticmethod
    def inserir_novo_livro(sistema, titulo, autor, genero, quantidade_disponivel):
        for livro_existente in sistema.lista_livros_total:
            if livro_existente.titulo == titulo:
                print("Livro com mesmo título já existe. Não é possível adicionar.")
                return

        try:
            quantidade_disponivel = int(quantidade_disponivel)
        except ValueError:
            print("A quantidade deve ser um número inteiro.")
            return

        livro = Livro(titulo, autor, genero, quantidade_disponivel)
        sistema.lista_livros_total.append(livro)
        print(f"Novo livro inserido: {livro}")
        return livro

    @staticmethod
    def visualizar_estoque(sistema):
        print("Estoque:")
        for livro in sistema.lista_livros_total:
            print(f"{livro} - Quantidade Disponível: {livro.quantidade_disponivel}")

    @staticmethod
    def aumentar_quantidade_estoque(sistema, titulo, quantidade):
        try:
            quantidade = int(quantidade)
        except ValueError:
            print("A quantidade deve ser um número inteiro.")
            return

        for livro in sistema.lista_livros_total:
            if livro.titulo == titulo:
                livro.quantidade_disponivel += quantidade
                print(f"Quantidade de {livro.titulo} aumentada para {livro.quantidade_disponivel}")
                return
        print("Livro não encontrado.")
