class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel=0, quantidade_comprada=0):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel
        self.quantidade_comprada = quantidade_comprada

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.genero})"
