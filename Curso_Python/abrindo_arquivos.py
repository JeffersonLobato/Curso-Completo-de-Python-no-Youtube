
texto = ''

while True:
    texto = input('Deseja continuar? S/N ')

    if texto.lower() == 'n':
        break

    else:
        with open('texto.txt', 'a') as arquivo:
            diario = input("O que deseja escrever no seu diário? Digite: ")
            arquivo.write('\n' + diario)
