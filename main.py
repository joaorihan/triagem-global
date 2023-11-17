from tkinter import *
import exames
import perguntas
import time

problemas = []

def opcao_1():
    # Adicione o código do Simulador da Triagem Automática aqui
    pass

def opcao_2():
    pass
    # Adicione o código que mostra informações sobre o Simulador aqui

def opcao_sair():
    print("\n| Saindo...")
    time.sleep(2)
    print("\n| Volte sempre!")
    time.sleep(1)
    exit()

while True:
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
        nome_paciente = input("Nome: ")
        idade_paciente = int(input("Idade: "))
        opcao_1()
    elif opcao == "2":
        opcao_2()
    elif opcao == "0" or opcao.upper() == "SAIR":
        opcao_sair()
        break #retirar
    else:
        print("\n| Opção inválida! Tente novamente.")
        time.sleep(2)


pacientes = {
    1 : {"nome":nome_paciente, "idade":idade_paciente, "diagnosticos" : problemas},
}




print("Bem Vindo(a) a central de atendimento automatizado da FIAP")
print("Você só precisa se identificar para iniciarmos nosso diagnóstico!")


print(f"Muito bem {nome_paciente}, agora, iremos fazer algumas perguntas")

print("\nPrimeiramente vamos começar medindo seus níveis de oxigênio.\nPor favor, coloque seu dedo na luz vermelha indicadora.")

time.sleep(1)


falta_oxigenio = exames.oximetria(idade_paciente)

altura_peso = exames.pesagem(idade_paciente)

print(altura_peso["altura"])
print(altura_peso["peso"])

sente_dor = perguntas.dores()

falta_ar = perguntas.falta_de_ar()

tem_diabetes = perguntas.diabetes()

fumante = perguntas.fuma()

alcoolatra = perguntas.alcool()

sedentario = perguntas.sedentarismo()


lista_perguntas = [falta_oxigenio, sente_dor, falta_ar, tem_diabetes, fumante, alcoolatra, sedentario]


for pergunta in lista_perguntas:
    if pergunta == True:
        problemas.append(pergunta.denominator)

#todo: fazer dicionário para valores dos problemas

print(problemas)


# window = Tk()
# window.title("Triagem Automática")
# window.geometry("1000x600+300+250")


# fonte = ("Arial, 13")

# window.mainloop()