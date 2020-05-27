nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# menor de 16 anos não vota
# entre 16 e 17 anos e acima de 64 voto opcional
# entre 18 e 65 voto obrigatório

if idade < 16:
    print(nome + ", você tem " + str(idade) + " anos e você não pode votar.")

elif (idade >= 16 and idade <= 17) or (idade > 64):
    print(nome + ", você tem " + str(idade) + " anos e seu voto é opcional.")

else:
    print(nome + ", você tem " + str(idade) + " anos e seu voto é obrigatório.")