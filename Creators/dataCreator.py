from datetime import datetime, timedelta , date
from view.exibir import exibirData

def criarDataEvento(nomeCliente):
    data_atual = datetime.today()
    data_formatada = data_atual.strftime("Horário atual: %d/%m/%Y %H:%M")
    
    print(data_formatada)
    
    ehCatolico = input("Digite C para casamento catolico e E para evangelico (C/E):   ").upper()
    yearEvent = int(input("Em que ano acontecerá o seu eventoFORMATO(YYYY)?:  "))
    
    if yearEvent < datetime.today().year:
    
        print(f"O ano do seu evento é inferior ao ano atual {data_atual}, tente novamente")
        exit(1)
    
    monthEvent = int(input("Em que mês acontecerá o seu evento(MM):  "))
    dayEvent = int(input("Em que dia acontecerá o seu evento(DD):  "))
    horarioInicialEvent = input("Qual será o horário de início do seu evento(HH:HH):  ")
    horarioFinalEvent = input("Qual será o horário de finalização do seu evento(HH:HH):  ")
    localEvento = input("Qual será o local do evento?").upper()
    valorEvento = float(input("Qual o valor do evento (R$XXXX.XX):  "))
    entrada = float(input("Quanto foi recebido de entrada:  "))
    qtd_musicos_festa= int(input("Quantos musicos irao para a FESTA (nao contar cantora):  ")) #incluindo tecladista
    qtd_musicos_cerimonia = int(input("Quantos musicas irao para a CERIMONIA :  "))
    tem_bv = float(input("Quanto foi o BV:  "))
    tem_alaan= float(input("QUANTO O ALAAN GANHOU:  "))
    tem_tecladista = (input("Tem tecladista?: (S/N) ")).upper()
    valor_som = float(input("Qual o valor do som?:  "))

    custo_musicos_cerimonia = (qtd_musicos_cerimonia + 1) * 200 # +1 PARA CONTAR COM A CANTORA
    custo_musicos_festa = ((qtd_musicos_festa + 1) * 350)

    if tem_tecladista == "S":
        custo_musicos_festa = ((qtd_musicos_festa + 1) * 350) + 100
        custo_musicos = custo_musicos_cerimonia + custo_musicos_festa
        lista_calculo_custo = [custo_musicos, tem_bv, tem_alaan, valor_som]
    else:
        custo_musicos = custo_musicos_cerimonia + custo_musicos_festa
        lista_calculo_custo = [custo_musicos, tem_bv, tem_alaan, valor_som ]

    
    lista_custo_real = []

    for item in lista_calculo_custo:
        if item != 0:
            lista_custo_real.append(item)
    
    custo_total = sum(lista_custo_real) #custo BV + ALAAN + MUSICOS + CANTORA + SOM

    h_inicio, m_inicio = map(int,(horarioInicialEvent.split(":")))
    h_fim, m_fim = map(int ,(horarioFinalEvent.split(":")))



    #criar logica para 15 dias antes do evento receber oq falta da entrada e logica para horas extras


    inicio = datetime(yearEvent, monthEvent, dayEvent, h_inicio, m_inicio)
    fim = datetime(yearEvent, monthEvent, dayEvent, h_fim, m_fim)

   

    if fim <= inicio:
    
        fim+=timedelta(days=1)
    

    if inicio.date() < date.today():
    
        print(f"Data invalida, pois esta ocorrendo antes da data atual {datetime.today()}")
        exit(1)

    duracao = fim - inicio
    dia_pagamento_valorFaltante = (inicio - timedelta(days=15))
    if duracao > timedelta(hours=4):
        horas_extras = duracao - timedelta(hours=4)
        custo_hora_extra = 100*horas_extras
        if custo_hora_extra != 0:
            resumo_evento = exibirData(inicio , fim, duracao, nomeCliente, localEvento, valorEvento, entrada, custo_total, custo_hora_extra, dia_pagamento_valorFaltante, ehCatolico)

    resumo_evento = exibirData(inicio , fim, duracao, nomeCliente, localEvento, valorEvento, entrada, custo_total, None, dia_pagamento_valorFaltante, ehCatolico)
    
    return nomeCliente ,resumo_evento, yearEvent, monthEvent
