import matematico

continuar = ""

while True:
    continuar = input("\nDeseja calcular? S/N ")

    if continuar.lower() == "n":
        break
    else:
        try:

            operacao = input("Qual operação deseja fazer? Digite\n1 para soma\n2 para subtração"
                             "\n3 para multiplicação\n4 para divisão\n")
            if operacao == "1":
                num1 = int(input("Digite um número: "))
                num2 = int(input("Digite outro número: "))
                print(matematico.soma(num1,num2))
                print("")

            elif operacao == "2":
                num1 = int(input("Digite um número: "))
                num2 = int(input("Digite outro número: "))
                print(matematico.sub(num1, num2))
                print("")

            elif operacao == "3":
                num1 = int(input("Digite um número: "))
                num2 = int(input("Digite outro número: "))
                print(matematico.mult(num1, num2))
                print("")

            elif operacao == "4":
                num1 = int(input("Digite um número: "))
                num2 = int(input("Digite outro número: "))
                print(matematico.div(num1, num2))
                print("")

            else:
                print("\nVocê digitou uma opção inválida, tente novamente.\n")

        except:
            print("\nOcorreu algum erro, verique a sua operação, como por exemplo,\nse houve tentativa"
                  " de divisão por zero, pois não é possível dividir por zero.")

print("\nObrigado por utilizar a calculadora de Jefferson Lobato")


