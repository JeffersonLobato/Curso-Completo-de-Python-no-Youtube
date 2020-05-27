dicio = {}

dicio["violão"] = "\nVIOLÃO\nsubstantivo masculino\n1.\nMÚSICA\n" \
                  "instrumento de cordas dedilháveis, com caixa de ressonância em\n" \
                  "formato semelhante a um oito, com seis cordas, de diferentes materiais.\n2.\n" \
                  "POR METONÍMIA•MÚSICA\nm.q. VIOLONISTA (subst.).\n3.\nPOR ANALOGIA\n" \
                  "(da acp. 1) B infrm. mulher de formas arredondadas, ancas largas e cintura fina.\n"

dicio["tecnologia"] = "\nTECNOLOGIA\nsubstantivo feminino\n1.\nteoria "\
                      "geral e/ou estudo sistemático sobre técnicas,"\
                      " processos, métodos, meios e\ninstrumentos de um"\
                      " ou mais ofícios ou domínios da atividade humana\n"\
                      "(p.ex., indústria, ciência etc.).\n2.\nPOR METONÍMIA\n"\
                      "técnica ou conjunto de técnicas de um domínio particular.\n"\
                      "a t. nutricional\n3.\nPOR EXTENSÃO\nqualquer técnica moderna e complexa.\n"


continuar = ""

while True:
    continuar = input("\nDeseja saber o signifado de alguma palavra? S/N ")

    if continuar.lower() == "n":
        break
    else:
        palavra = input("Digite uma palavra: ")

        if palavra.lower() in dicio:
            print(dicio[palavra.lower()])
        else:
            print("\nA palavra " + palavra + " não existe em nosso banco de dados, tente novamente.")


print("\nObrigado por ter utilizado o dicionário do Jefferson Lobato. Volte sempre!\n")