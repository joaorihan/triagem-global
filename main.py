import exames
import perguntas
import time
import re

string_problemas = ""
problemas = []
    

def validar_nome(nome):
    import re
    return bool(re.match("^[a-zA-ZÀ-ÖØ-öø-ÿ]+$", nome))


def validar_idade(idade):
    import re
    return bool(re.match("^\\d+$", idade))


def prontuario(string_problemas, problemas, nome_paciente, idade_paciente):
    estado = "Observação"
    if sente_dor:
        string_problemas += ("| Dor agúda detectada... Receitando Anti-Inflamatório\n")
        problemas.append("Paciente Sente Dores; ")
        estado = "Alerta"
    if falta_oxigenio:
        string_problemas += ("| Taxa de oxigênio baixa. Alerta\n")
        problemas.append("Paciente com baixa em Oximetro; ")
        estado = "Alerta"
    if tem_diabetes:
        string_problemas += ("| Paciente tem histórico de diabetes. Recomendação: Pegar amostra sanguínea.\n")
        problemas.append("Paciente tem Diabetes; ")
    if falta_ar and fumante:
        string_problemas += ("| Recomendação: Evite fumar cigarros nos próximos dias\n")
        problemas.append("Paciente sente falta de ar e é um Fumante ativo; ")

    print(f"\n| Prontuário do(a) paciente {nome_paciente.lower().capitalize()}\n| \n| Idade: {idade_paciente}\n| Estado: {estado}\n| ")
    print(string_problemas)



def prontuario_json(nome_paciente, idade_paciente, problemas):
    import json
    import os

    try:
        pacientes = {
            1 : {"nome":nome_paciente, "idade":idade_paciente, "diagnosticos" : problemas}
        }
        with open('pacientes.json','w', encoding='utf-8') as arquivo_saida:
            arquivo_saida.write(json.dumps(pacientes))
    except FileExistsError:
        print("Arquivo já existe")
        os.remove("pacientes.json")


def opcao_info():
    import time
    print("Informações Sobre o Simulador\n\n\n texto...")
    time.sleep(1)
    input("Pressione 'Enter' para voltar ao menu")

def opcao_sair():
    import time
    print("\n| Saindo...")
    time.sleep(2)
    print("\n| Volte sempre!")
    time.sleep(1)
    exit()

    

while True:

    #Menu de opções 

    print("\n")
    print("| Central de Atendimento da FIAP")
    print("| Escolha uma opção para começar.")
    print("| ")
    print("| [1] - Simulador da Triagem Automática")
    print("| [2] - Informações Sobre o Simulador")
    print("| ")
    print("| [0] - Sair")

    opcao = input()

    if opcao == "1":

        print("Bem Vindo(a) a central de atendimento automatizado da FIAP")
        print("Você só precisa se identificar para iniciarmos nosso diagnóstico!")
        #Valdação das entradas de dados do usuário.
        nome_paciente = input("Nome: ")
        while not validar_nome(nome_paciente):
            print("Erro! O nome deve conter apenas letras.")
            nome_paciente = input("Nome: ")

        idade_paciente = input("Idade: ")
        while not validar_idade(idade_paciente):
            print("Erro! A idade deve conter apenas números.")
            idade_paciente = input("Idade: ")
        idade_paciente = int(idade_paciente)

        print(f"Muito bem {nome_paciente.lower().capitalize()}, agora, realizaremos algumas medições.")

        print("\nPrimeiramente vamos começar medindo seus níveis de oxigênio.\nPor favor, coloque seu dedo na luz vermelha indicadora.")

        time.sleep(1)


        falta_oxigenio = exames.oximetria(idade_paciente)
        altura_peso = exames.pesagem(idade_paciente)

        print(f"\n{nome_paciente.lower().capitalize()}, agora, faremos algumas perguntas.")


        sente_dor = perguntas.dores()
        falta_ar = perguntas.falta_de_ar()
        tem_diabetes = perguntas.diabetes()
        fumante = perguntas.fuma()
        alcoolatra = perguntas.alcool()
        sedentario = perguntas.sedentarismo()
        
        prontuario(string_problemas, problemas, nome_paciente, idade_paciente)
        prontuario_json(nome_paciente, idade_paciente, problemas)

        input("Pressione 'Enter' para voltar ao menu")
    elif opcao == "2":
        opcao_info()
    elif opcao == "0" or opcao.upper() == "SAIR":
        opcao_sair()
    else:
        print("\n| Opção inválida! Tente novamente.")
        time.sleep(2)

print("\n\nFim do Programa")        