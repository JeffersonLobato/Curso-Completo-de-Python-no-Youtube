class Carros():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro"""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.combustivel = 100
        self.odometro = 0

    def descricao_nome(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        nome_longo = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_longo.title()

    def leia_odometro(self):
        """Exibe uma frase que mostra o valor do odômetro do carro"""
        print("O carro tem " + str(self.odometro) + " KM rodados.")

    def altera_odometro(self,novo_odometro):
        """Alterar o odômetro pelo valor passado como argumento."""
        self.odometro = novo_odometro

    def incrementa_odometro(self,novo_odometro):
        """Incrementa um determinado valor ao odômetro."""
        self.odometro += novo_odometro


    def tanque_gasolina(self):
        """Exibe a quantidade de gasolina no tanque"""
        print("O tanque de gasolina está " + str(self.combustivel) + "% cheio.")



class CarrosEletricos(Carros):
    """Representa aspectos de um carro específico, no casso, carro elétrico"""
    def __init__(self,fabricante, modelo, ano):
        """Inicializa os atributos da classe-pai"""
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()

    def tanque_gasolina(self):
        """Carros elétricos não usam gasolina."""
        print("Carros elétricos não usam gasolina.")


class Bateria():
    """Uma tentativa simples de criar uma bateria"""
    def __init__(self,bateria=100):
        """Inicializa os atributos da bateria"""
        self.bateria = bateria

    def altera_bateria(self, novo_valor):
        """Altera o valor da bateria"""
        self.bateria = novo_valor

    def mostra_bateria(self):
        print("A bateria do carro está " + str(self.bateria) + "% cheia.")


