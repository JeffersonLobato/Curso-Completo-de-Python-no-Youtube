import matematico

continuar = ""

while True:
    continuar = input("\nDeseja jogar par ou ímpar? S/N ")
    if continuar.lower() == "n":
        break
    else:
        jogador1 = input("\nDigite o nome do jogador 1: ")
        jogador2 = input("Digite o nome do jogador 2: ")
        par_ou_impar = input(jogador1 + " Digite 1 para ímpar e 2 para par: ")

        if par_ou_impar != "1" and par_ou_impar != "2":
            print("Você digitou uma opção inválida")
            continue

        else:
            num_jog1 = int(input(jogador1 + " digite um número qualquer: "))
            num_jog2 = int(input(jogador2 + " digite um número qualquer: "))
            soma = matematico.soma(num_jog1,num_jog2)
            resultado = matematico.par_impar(num_jog1, num_jog2)
            print("\nO " + jogador1 + " escolheu " + str(num_jog1) + " e o " + jogador2 + " escolheu " + str(num_jog2))
            print("e a soma da " + str(soma) + " que é " + resultado)

            if resultado == "PAR":
                if par_ou_impar == "1":
                    print("\nParabéns " + jogador2 + " você é o vencedor!")
                else:
                    print("\nParabéns " + jogador1 + " você é o vencedor!")
            else:
                if par_ou_impar == "1":
                    print("\nParabéns " + jogador1 + " você é o vencedor!")
                else:
                    print("\nParabéns " + jogador2 + " você é o vencedor!")


print("\nEspero que tenha se divertido, volte mais vezes")