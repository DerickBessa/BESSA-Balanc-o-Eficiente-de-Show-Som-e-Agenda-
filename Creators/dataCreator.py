from datetime import datetime, timedelta , date
from exibir import exibirData

def criarDataEvento(nomeCliente):
    data_atual = datetime.today()
    data_formatada = data_atual.strftime("Horário atual: %d/%m/%Y %H:%M")
    
    print(data_formatada)
    
    ehCatolico = input("Digite C para casamento catolico e E para evangelico (C/E):   ").upper()
    yearEvent = int(input("Em que ano acontecerá o seu evento? FORMATO(YYYY)"))
    
    if yearEvent < datetime.today().year:
    
        print(f"O ano do seu evento é inferior ao ano atual {data_atual}, tente novamente")
        exit(1)
    
    monthEvent = int(input("Em que mês acontecerá o seu evento? FORMATO (MM)"))
    dayEvent = int(input("Em que dia acontecerá o seu evento? FORMATO(DD)"))
    horarioInicialEvent = input("Qual será o horário de início do seu evento? FORMATO:(XX:XX)")
    horarioFinalEvent = input("Qual será o horário de finalização do seu evento? FORMATO:(XX:XX)")
    localEvento = input("Qual será o local do evento?").upper()
    valorEvento = float(input("Qual o valor do evento (R$XXXX.XX): "))
    entrada = float(input("Quanto foi recebido de entrada: "))
    
    h_inicio, m_inicio = map(int,(horarioInicialEvent.split(":")))
    h_fim, m_fim = map(int ,(horarioFinalEvent.split(":")))

    inicio = datetime(yearEvent, monthEvent, dayEvent, h_inicio, m_inicio)
    fim = datetime(yearEvent, monthEvent, dayEvent, h_fim, m_fim)

    if fim <= inicio:
    
        fim+=timedelta(days=1)
    

    if inicio.date() < date.today():
    
        print(f"Data invalida, pois esta ocorrendo antes da data atual {datetime.today()}")
        exit(1)

    duracao = fim - inicio

    resumo_evento = exibirData(inicio , fim, duracao, nomeCliente, localEvento, valorEvento, entrada, ehCatolico)
    
    return ehCatolico, nomeCliente ,resumo_evento
