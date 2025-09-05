from datetime import date, datetime
import os
# from Creators.pdfcreator import pdfEventCreator

def exibirData (inicio, fim, duracao, nomeCliente, localEvento,valorEvento,entrada,custo_total,custo_hora_extra, dia_pagamento_faltante, ehCatolico):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if custo_hora_extra == None:
        custo_hora_extra = 0

    lucro = valorEvento - custo_total + custo_hora_extra

    entradaPorcentagem = (entrada*100/valorEvento)
    restanteEntrada = ((30 - entradaPorcentagem)/100) * valorEvento
    pagamento_faltante = valorEvento - entrada

    inicio_fmt = inicio.strftime("%d/%m/%Y às %H:%M")
    fim_fmt    = fim.strftime("%d/%m/%Y às %H:%M")
    dia_pagamento_faltante = dia_pagamento_faltante.strftime("%d/%m/%Y")
    dia_pagamento_faltante = dia_pagamento_faltante + f"Faltam R${pagamento_faltante}"

    if ehCatolico == "C":
        ehCatolico = "Catolica"
    elif ehCatolico == "E":
        ehCatolico = "Evangelica"

    
   
    if entradaPorcentagem < 30:
        entradaPaga = (f"foram pagos {entradaPorcentagem}% faltam {(restanteEntrada*100 / valorEvento)}%")
    else:
        entradaPaga = (f"foram pagos {entradaPorcentagem} de R${valorEvento}")

    h, resto = divmod(duracao.seconds, 3600)
    m, _     = divmod(resto, 60)

    valorTotalStr = ("R$"+str(valorEvento))
    duracao = f"{h}h {m}min"
    
    resumo_evento = {
        "Cliente": nomeCliente,
        "Religião": ehCatolico,
        "Valor total": valorEvento,
        "Entrada valor": entrada,
        "Entrada situacao": entradaPaga,
        "Local": localEvento,
        "Início": inicio_fmt,
        "Fim": fim_fmt,
        "Duração": duracao,
        "Custo" : custo_total,
        "Lucro" : lucro,
        "Data pagamento faltante": dia_pagamento_faltante
     }


    # Exibindo de forma organizada
    print("-"*60)
    print(f"RESUMO DO EVENTO DE {nomeCliente}:")
    print("-"*60)
    for campo, info in resumo_evento.items():
        print(f"{campo:15}: {info}")
    print("-"*60)
    print("Evento salvo na planilha excel com sucesso!!")

    end = input("Para finalizar digite E e aperte enter!: ")
    # pdfEventCreator(resumo_evento, nomeCliente)
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
       
        

def cabecalhoReinicio():
        print("|",40*f"-", f"\n|")
        print("|",10*" ", f"B. E. S. S. A.\n|")
        print("|",f"Balanço Eficiente de Show Som e Agendas")
        print("|",40*f"-", f"\n|")
        print("Pressione F para reiniciar ou qualquer outra tecla para sair.")
        escolha = input("| Sua escolha: ").upper()
        return escolha