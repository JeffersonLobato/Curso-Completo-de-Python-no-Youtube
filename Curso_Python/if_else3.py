#Ingredientes pedidos pelo usuário
ingred_pedido = []
continuar = "s"

while continuar.lower() == "s":

    ing = input("Digite um ingrediente de sua preferência: ")
    ingred_pedido.append(ing.lower())
    continuar = input("Deseja continua? s ou n ")

#Ingredientes da pizzaria
ingredientes = ["mostarda", "pimentão","queijo extra"]

for ingrediente in ingred_pedido:

    if ingrediente in ingredientes:
        print("Adicionando " + ingrediente + " a sua pizza.")
    else:
        print("Sinto muito, não temos " + ingrediente + ".")


print("\nSua pizza está pronta.")