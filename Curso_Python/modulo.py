def lista_funcao(lista):
    for cor in lista:
        print(cor)

def nome_completo(primeiro_nome="", ultimo_nome="", nome_do_meio=""):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != "":
        nome_completo = "O nome digitado foi " + primeiro_nome.title() + " " + nome_do_meio.title() + " " + ultimo_nome.title()

    else:
        nome_completo = "O nome digitado foi " + primeiro_nome.title() + " " + ultimo_nome.title()

    return nome_completo

def nome_completo(primeiro_nome="", ultimo_nome="", nome_do_meio=""):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != "":
        print("O nome digitado foi " + primeiro_nome.title() + " " + nome_do_meio.title() + " " + ultimo_nome.title())

    else:
        print("O nome digitado foi " + primeiro_nome.title() + " " + ultimo_nome.title())

def soma(num1, num2):
    soma1 = num1
    soma2 = num2
    soma_total = soma1 + soma2
    return soma_total

def sub(num1, num2):
    sub1 = num1
    sub2 = num2
    sub_total = sub1 - sub2
    return sub_total

def mult(num1, num2):
    mult1 = num1
    mult2 = num2
    mult_total = mult1 * mult2
    return mult_total

def div(num1, num2):
    div1 = num1
    div2 = num2
    div_total = div1/div2
    return div_total