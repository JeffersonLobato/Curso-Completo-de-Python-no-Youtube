lista_cor = ["Vermelho","Verde","Preto","Branco","Azul"]
print(lista_cor)
def lista_funcao(lista):
    for cor in lista:
        print(cor)

lista_funcao(lista_cor[:])
print(lista_cor)