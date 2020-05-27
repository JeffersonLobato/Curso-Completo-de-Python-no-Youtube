def nome_completo(primeiro_nome="", ultimo_nome="", nome_do_meio=""):
    primeiro_nome = primeiro_nome
    ultimo_nome = ultimo_nome
    nome_do_meio = nome_do_meio

    if nome_do_meio != "":
        nome_completo = "O nome digitado foi " + primeiro_nome.title() + " " + nome_do_meio.title() + " " + ultimo_nome.title()

    else:
        nome_completo = "O nome digitado foi " + primeiro_nome.title() + " " + ultimo_nome.title()

    return nome_completo

nome = nome_completo("Jefferson","Batista","Lobato")

print(nome)