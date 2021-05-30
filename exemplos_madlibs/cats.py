def madlib():
    parte_gato = input("Parte do gato: ")
    verbo = input("verbo: ")
    adj1 = input("Adjetivo: ")
    adj2 = input("Adjetivo: ")
    adj3 = input("Adjetivo: ")
    adj4 = input("Adjetivo: ")
    adj5 = input("Adjetivo: ")
    substantivo1 = input("Substantivo: ")
    substantivo2 = input("Substantivo: ")
    substantivo3 = input("Substantivo: ")
    subst_plural1 = input("Substantivo no plural: ")
    subst_plural2 = input("Substantivo no plural: ")
    subst_plural3 = input("Substantivo no plural: ")

    madlib = f"Eu amo um gato com {parte_gato}! Toda vez que vejo um gatinho {adj1} na rua, \
eu sempre vou {adj2} em direção à ele segurando um {substantivo1} para tentar conquistá-lo. \
Uma vez, eu estava {adj3} quando vi um {substantivo2} na casa de um parente {adj4} que tinha gatos! \
Um monte de gatos com {subst_plural1} acabou me dando um {substantivo3} enquanto eu fiquei {adj5}...\
Desde esse dia, eu guardo na bolsa {subst_plural2} esperando {verbo}, enquanto penso naquele lugar que me faz pensar em \
{subst_plural3} que os gatos costumam ter..."

    print(madlib)


madlib()
