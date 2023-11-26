from UsuarioAdministrador import UsuarioAdministrador

class UsuarioCliente:
    @staticmethod
    def comprar_livro(sistema, titulo):
        for livro in sistema.lista_livros_total:
            if livro.titulo == titulo:
                if livro.quantidade_disponivel > 0:
                    livro.quantidade_comprada += 1
                    livro.quantidade_disponivel -= 1
                    print(f"{livro.titulo} comprado com sucesso!")
                else:
                    print(f"{livro.titulo} está indisponível.")
                return
        print("Livro não encontrado.")

    @staticmethod
    def listar_livros_comprados(sistema):
        print("Livros comprados:")
        livros_comprados = []
        for livro in sistema.lista_livros_total:
            if livro.quantidade_comprada > 0:
                livros_comprados.append(livro)
                print(f"{livro.titulo} - Quantidade Comprada: {livro.quantidade_comprada}")
        return livros_comprados

    @staticmethod
    def ver_dados_livro(sistema, titulo):
        for livro in sistema.lista_livros_total:
            if livro.titulo == titulo:
                print(f"Dados de {livro.titulo}:")
                print(f" - Gênero: {livro.genero}")
                print(f" - Autor: {livro.autor}")
                return [livro.titulo, livro.autor, livro.genero]
        print("Livro não encontrado.")
        return None

    @staticmethod
    def visualizar_estoque(sistema):
        UsuarioAdministrador.visualizar_estoque(sistema)
