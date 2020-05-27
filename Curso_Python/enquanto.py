
while True:
    print("Para encerrar digite sair\n")
    cidade = input("Digite uma cidade: ")
    print("")

    if cidade == 'continuar':
        continue
    elif cidade == 'sair':
        break
    else:
        print("A cidade digitada foi " + cidade + "\n")

print('\nESTOU FORA DO LAÇO E ENCERRANDO')