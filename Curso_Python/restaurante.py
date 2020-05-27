class Restaurante():
    """Representa um restaurante"""
    def __init__(self, restaurante_nome, tipo_cozinha):
        self.restaurante_nome = restaurante_nome
        self.tipo_cozinha = tipo_cozinha

    def restaurante_descricao(self):
        print("O restaurante se chama " + self.restaurante_nome + " e sua especialidade é " + self.tipo_cozinha)

    def restaurante_aberto(self):
        print("O restaurante " + self.restaurante_nome + " está aberto no momento!")



restaurante1 = Restaurante("La casa do pastel", "pastel")
restaurante2 = Restaurante("Comida à mineira", "comida mineira")
restaurante3 = Restaurante("Massa Fera", "massas")

restaurante1.restaurante_descricao()
restaurante2.restaurante_descricao()
restaurante3.restaurante_descricao()