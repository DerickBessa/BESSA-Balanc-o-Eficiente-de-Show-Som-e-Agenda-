from dataCreator import criarDataEvento 
from exibir import cabecalhoFinalizar, cabecalhoIniciar, cabecalhoDefault
from cerimonia import cerimoniaCreator, exibirRepertorio
from datetime import date, datetime, timedelta
from bancoDados import criar_tabelas, inserir_evento, inserir_repertorio
import os

criar_tabelas()

os.system('cls' if os.name == "nt" else 'clear')
cabecalhoDefault()
start = input("| Deseja criar uma data? (S/N):  ").upper()

if start == 'S':
    os.system('cls' if os.name == "nt" else 'clear')
    cabecalhoIniciar("E")
    nomeCliente= input("Qual o nome do contratante?").upper()
    ehCatolico, nomeCliente, resumo_evento= criarDataEvento(nomeCliente) #essa funcao tambem retorna o nomeCliente novamente para consulta em um futuro banco de dados
    event_id = inserir_evento(resumo_evento)
    cabecalhoDefault()
    skip = input("| Deseja organizar a cerimonia? (S/N)").upper()
    if skip == "S":
        os.system('cls' if os.name == "nt" else 'clear')
        cabecalhoIniciar("C")
        repertorio, nomeCliente = cerimoniaCreator(ehCatolico , nomeCliente)
        inserir_repertorio(event_id, repertorio)
        exibirRepertorio(repertorio, nomeCliente)
        os.system('cls' if os.name == "nt" else 'clear')
        cabecalhoFinalizar("E")
    else:
        os.system('cls' if os.name == "nt" else 'clear')
        cabecalhoFinalizar("E")
        exit(1)

else:
    os.system('cls' if os.name == "nt" else 'clear')
    cabecalhoDefault()
    skip = input("| Deseja organizar a cerimonia? (S/N)").upper()
    if skip == "S":
        ehCatolico = input("Digite C para catolica e E para evangelica (C/E): ").upper()
        os.system('cls' if os.name == "nt" else 'clear')
        if ehCatolico == "C" or ehCatolico == "E":
            cabecalhoIniciar('C')
            repertorio, nomeCliente =cerimoniaCreator(ehCatolico)
            exibirRepertorio(repertorio, nomeCliente)
            cabecalhoFinalizar("C")
        else:
            print("Digite uma letra valida entre C e E.")
    else:
        cabecalhoFinalizar("C")
        exit(1)

    
