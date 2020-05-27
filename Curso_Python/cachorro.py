class Cachorro():
    """Uma tentativa simples de modelar um cachorro."""
    def __init__(self, nome, idade):
        """Inicializa os atributos nome e idade"""
        self.nome = nome
        self.idade = idade

    def sentar(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.nome.title() + " está sentando.")

    def rolar(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.nome.title() + " está rolando.")


meu_cachorro = Cachorro("Aquiles", 6)

meu_cachorro.rolar()
meu_cachorro.sentar()

meu_outro_cachorro = Cachorro("Bingo", 5)

meu_outro_cachorro.rolar()
meu_outro_cachorro.sentar()