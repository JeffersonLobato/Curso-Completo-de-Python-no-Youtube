convidados = []

print("Quando terminar digite FIM\n")

while True:
    convidado = input("Digite o nome do convidado ou digite FIM: ")

    if convidado.lower() == "fim":
        break

    else:
        convidados.append(convidado.title())

convidados.sort()

print("\n############ LISTA DE CONVIDADOS #############\n")

for convidado in convidados:
    print(">>>>>>>>>  " + convidado)