from tkinter import *
import exames
import perguntas
import time

print("Bem Vindo(a) a central de atendimento automatizado da FIAP")
print("Você só precisa se identificar para iniciarmos nosso diagnóstico!")
nome_paciente = input("Nome: ")
idade_paciente = int(input("Idade: "))


print(f"Muito bem {nome_paciente}, agora, iremos fazer algumas perguntas")

print("\nPrimeiramente vamos começar medindo seus níveis de oxigênio.\nPor favor, coloque seu dedo na luz vermelha indicadora.")

time.sleep(1)


falta_oxigenio = exames.oximetria(idade_paciente)

peso_altura = exames.pesagem(idade_paciente)

print(peso_altura)
print(type(peso_altura))

sente_dor = perguntas.dores()

falta_ar = perguntas.falta_de_ar()

tem_diabetes = perguntas.diabetes()

fumante = perguntas.fuma()

alcoolatra = perguntas.alcool()

sedentario = perguntas.sedentarismo()


lista_perguntas = [falta_oxigenio, sente_dor, falta_ar, tem_diabetes, fumante, alcoolatra, sedentario]

problemas = []

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