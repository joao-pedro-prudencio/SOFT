from Sistema import Sistema
from UsuarioAdministrador import UsuarioAdministrador
from UsuarioCliente import UsuarioCliente

def main():
    sistema = Sistema()

    while True:
        print("\nMenu Principal:")
        print("1. Entrar como Administrador")
        print("2. Entrar como Cliente")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_adm(sistema)
        elif escolha == "2":
            menu_cliente(sistema)
        elif escolha == "3":
            print("Programa finalizado")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_adm(sistema):
    while True:
        print("\nMenu Administrador:")
        print("1. Inserir novo livro")
        print("2. Visualizar estoque")
        print("3. Aumentar quantidade de livro no estoque")
        print("4. Voltar para o Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            genero = input("Digite o gênero do livro: ")
            quantidade_disponivel = input("Digite a quantidade disponível: ")
            UsuarioAdministrador.inserir_novo_livro(sistema, titulo, autor, genero, quantidade_disponivel)
        elif opcao == "2":
            UsuarioAdministrador.visualizar_estoque(sistema)
        elif opcao == "3":
            titulo = input("Digite o título do livro: ")
            quantidade = input("Digite a quantidade a ser adicionada: ")
            UsuarioAdministrador.aumentar_quantidade_estoque(sistema, titulo, quantidade)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_cliente(sistema):
    while True:
        print("\nMenu Cliente:")
        print("1. Comprar livro")
        print("2. Listar livros comprados")
        print("3. Ver dados de um livro")
        print("4. Visualizar estoque")
        print("5. Voltar para o Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro que deseja comprar: ")
            UsuarioCliente.comprar_livro(sistema, titulo)
        elif opcao == "2":
            UsuarioCliente.listar_livros_comprados(sistema)
        elif opcao == "3":
            titulo = input("Digite o título do livro que deseja ver os dados: ")
            UsuarioCliente.ver_dados_livro(sistema, titulo)
        elif opcao == "4":
            UsuarioCliente.visualizar_estoque(sistema)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
