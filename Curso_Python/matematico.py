def soma(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    return soma

def sub(num1, num2):
    num1 = num1
    num2 = num2
    sub = num1 - num2
    return sub

def mult(num1, num2):
    num1 = num1
    num2 = num2
    mult = num1 * num2
    return mult

def div(num1, num2):
    num1 = num1
    num2 = num2
    div = num1/num2
    return div

def par_impar(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1+num2
    sobra = soma%2

    if sobra == 0:
        par_impar = "PAR"
    else:
        par_impar = "ÍMPAR"
    return par_impar