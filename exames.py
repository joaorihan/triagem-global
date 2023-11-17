def oximetria(idade_paciente):
    import random
    import time

    time.sleep(1)
    print("\nPor favor, não retire seu dedo da leitora")
    input("\nPressione 'Enter' para iniciar a medição")

    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(2)

    oxigenio = random.randint(92,100)

    if oxigenio < 95:
        print(f"Seus níveis de oxigênio estão muito baixos! {oxigenio}%")
        if idade_paciente < 60:
            alerta = False
            print("É recomendado prosseguir com ...")
        if idade_paciente >= 60:
            alerta = True
            print("Cuidado! Prossiga para o tratamentos")
    elif oxigenio >= 95:
        print(f"Níveis de oxigênio estão estáveis. {oxigenio}%")    
        alerta = False

    return alerta


def pesagem(idade_paciente):
    import random 
    import time
    idade_paciente = int(idade_paciente)

    time.sleep(1)
    print("\nAgora iremos fazer sua pesagem, juntamente com a medição de sua altura.\nPor favor, suba na balança ao lado.")
    input("\nPressione 'Enter' para iniciar a pesagem")

    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(2)

    if idade_paciente > 0 and idade_paciente < 12:
        peso = random.randint(25,35)
        altura = random.randint(110, 140)/100
    if idade_paciente >= 13 and idade_paciente < 18: 
        peso = random.randint(35, 45)
        altura = random.randint(145, 165)/100
    if idade_paciente >= 18:
        peso = random.randint(55, 100)
        altura = random.randint(155, 190)/100

    print(f"\nMedição e pesagem finalizados.\nAltura: {altura}\nPeso: {peso}")

    return {"altura" : altura, "peso": peso}


def prontuario(problemas):
    pass



