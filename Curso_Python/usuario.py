class Usuario():
    def __init__(self, primeiro_nome, ultimo_nome, idade, cidade, sexo):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo

    def descricao_usuario(self):
        print(self.primeiro_nome.title() + " " + self.ultimo_nome.title())
        print(str(self.idade) + " anos")
        print("Nascido em " + self.cidade)
        print("Do sexo " + self.sexo)

    def saudacao_usuario(self):
        print("Olá " + self.primeiro_nome.title() + " " + self.ultimo_nome.title() + ", seja bem vindo!")


usuario1 = Usuario("João", "Batista", 30, "Rio de Janeiro", "masculino")
usuario2 = Usuario("Julia", "Silva", 47, "São Paulo", "feminino")
usuario3 = Usuario("Alfredo", "Costa", 53, "Manaus", "masculino")

usuario1.descricao_usuario()
print("")
usuario2.descricao_usuario()
print("")
usuario3.descricao_usuario()