
def dores():
    import time
    print("\nNeste momento, você sente algum tipo de dor?")
    resposta = input("(S/N) ").upper()

    if resposta == "S" or resposta == "SIM":
        escala = int(input("Em uma escala de 1 a 5, o quão intensa é a sua dor? "))
        dor = True
    else: 
        time.sleep(1)
        print("...próxima pergunta") 
        dor = False

    return dor


def falta_de_ar():
    print("\nVocê sente alguma falta de ar?")
    resposta = input("(S/N) ").upper()           

    if resposta == "S" or resposta == "SIM":
        falta_ar = True
    else:
        falta_ar = False

    return falta_ar


def diabetes():
    print("\nVocê é diagnosticado(a) com Diabetes?")
    resposta = input("(Sim/Não/Não sei)").upper()

    if resposta == "S" or resposta == "SIM":
        tem_diabetes = True
    elif resposta == "N" or resposta == "NÃO":
        tem_diabetes = False
    else:
        tem_diabetes = False

    return tem_diabetes


def fuma():
    print("\nVocê é um fumante ativo?")
    resposta = input("(S/N) ").upper()
    
    if resposta in ["S", "SIM"]:
        quantos = int(input("Você costuma fumar, em média, quandos cigarros por dia? "))
        if quantos >= 10: 
            fumante = True
        else:
            fumante = False
    else:
        fumante = False

    return fumante


def alcool():
    print("\nVocê costuma ingerir bebidas alcoólicas com frequência? ")
    resposta = input("(S/N) ").upper()
    
    if resposta in ["S", "SIM"]:
        quantos = int(input("Você costuma beber, em média, quantas vezes na semana? "))
        if quantos >= 5:
            alcoolatra = True
        else:
            alcoolatra = False
    else:
        alcoolatra = False

    return alcoolatra


def sedentarismo():
    print("\nVocê pratica atividades físicas com frequência? ")
    resposta = input("(S/N) ")

    if resposta in ["S", "SIM"]:
        sedentario = False
    else:
        sedentario = True

    return sedentario