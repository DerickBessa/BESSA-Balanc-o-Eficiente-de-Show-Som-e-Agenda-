from datetime import date, datetime
import os
from pdfcreator import pdfEventCreator

def exibirData (inicio, fim, duracao, nomeCliente, localEvento,valorEvento,entrada, ehCatolico):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    inicio_fmt = inicio.strftime("%d/%m/%Y às %H:%M")
    fim_fmt    = fim.strftime("%d/%m/%Y às %H:%M")

    if ehCatolico == "C":
        ehCatolico = "Catolica"
    elif ehCatolico == "E":
        ehCatolico = "Evangelica"

    entradaPorcentagem = (entrada*100/valorEvento)
    restanteEntrada = ((30 - entradaPorcentagem)/100) * valorEvento
    
   
    if entradaPorcentagem < 30:
        entradaPaga = (f"foram pagos {entradaPorcentagem}% faltam R${restanteEntrada} , {(restanteEntrada*100 / valorEvento)}%")
    else:
        entradaPaga = (f"foram pagos {entradaPorcentagem} de R${valorEvento}")

    h, resto = divmod(duracao.seconds, 3600)
    m, _     = divmod(resto, 60)

    valorTotalStr = ("R$"+str(valorEvento))
    duracao = f"{h}h {m}min"
    
    resumo_evento = {
        "Cliente": nomeCliente,
        "Religião": ehCatolico,
        "Valor total": valorTotalStr,
        "Entrada valor": entrada,
        "Entrada situacao": entradaPaga,
        "Local": localEvento,
        "Início": inicio_fmt,
        "Fim": fim_fmt,
        "Duração": duracao
    }


    # Exibindo de forma organizada
    print("-"*60)
    print(f"RESUMO DO EVENTO DE {nomeCliente}:")
    print("-"*60)
    for campo, info in resumo_evento.items():
        print(f"{campo:15}: {info}")
    print("-"*60)

    end = input("Para finalizar digite E e aperte enter!: ")
    print("PDF gerado com sucesso!!")
    pdfEventCreator(resumo_evento, nomeCliente)
    if end == 'E':
        os.system('cls' if os.name == "nt" else 'clear')

    return resumo_evento
        

def cabecalhoIniciar(tipo):
    if tipo == "C":
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")
        print("|",5*" " , f"CRIAÇÃO DE CERIMONIA INICIADA\n|")
    elif tipo == "E":
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")
        print("|",5*" " , f"CRIAÇÃO DE EVENTO INICIADA\n|")

def cabecalhoFinalizar(tipo):
    if tipo == "C":
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")
        print("|",5*" " , f"CRIAÇÃO DE CERIMONIA FINALIZADA\n|")
    elif tipo == "E":
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")
        print("|",5*" " , f"CRIAÇÃO DE EVENTO FINALIZADA\n|")
def cabecalhoDefault():
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")