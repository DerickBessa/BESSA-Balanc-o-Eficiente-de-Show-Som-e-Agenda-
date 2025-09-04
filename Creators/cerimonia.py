from pdfcreator import pdfRepertorioCreator

import os
def cerimoniaCreator(ehCatolico, nomeCliente):
    repertorio = []
    if nomeCliente is None:
        nomeCliente = input("Qual o nome do Cliente?").upper()

    if ehCatolico == 'C':
       
        musicaPais = input("Qual será a música de entrada dos PAIS: ")
        musicaPadrinhos = input("Qual será a música de entrada dos PADRINHOS: ")
        musicaNoivo = input("Qual será a música de entrada do NOIVO: ")
        musicaNoiva = input("Qual será a música de entrada da NOIVA: ")
        musicaAlianca= input("Qual será a música de entrada da ALIANÇA: ")
        musicaAclamacao = input("Qual será a música de entrada dos ACLAMAÇÃO: ")
        musicaComunhao = input("Qual será a música de entrada da COMUNHÃO: ")
        musicaAssinatura = input("Qual será a música de entrada dos ASSINATURA: ")
        musicaSaida = input("Qual será a música de entrada dos SAIDA: ")
        repertorio = {
            "Pais": [musicaPais],
            "Padrinhos": [musicaPadrinhos],
            "Noivo": [musicaNoivo],
            "Noiva": [musicaNoiva],
            "Aliança": [musicaAlianca],
            "Aclamação": [musicaAclamacao],
            "Comunhão": [musicaComunhao],
            "Assinatura": [musicaAssinatura],
            "Saída": [musicaSaida]
        }

    else:
    
        musicaPais = input("Qual será a música de entrada dos PAIS: ")
        musicaPadrinhos = input("Qual será a música de entrada dos PADRINHOS: ")
        musicaNoivo = input("Qual será a música de entrada do NOIVO: ")
        musicaNoiva = input("Qual será a música de entrada da NOIVA: ")
        musicaAlianca= input("Qual será a música de entrada da ALIANÇA: ")
        musicaAssinatura = input("Qual será a música de entrada dos ASSINATURA: ")
        musicaSaida = input("Qual será a música de entrada dos SAIDA: ")
        repertorio = {
            "Pais": [musicaPais],
            "Padrinhos": [musicaPadrinhos],
            "Noivo": [musicaNoivo],
            "Noiva": [musicaNoiva],
            "Aliança": [musicaAlianca],
            "Assinatura": [musicaAssinatura],
            "Saída": [musicaSaida]
        }
   
    return repertorio, nomeCliente
    
def exibirRepertorio(repertorio, nomeCliente):
    
    print("REPERTORIO ATUAL: ")
    for item, itemMusica in repertorio.items():
        for musica in itemMusica:
            print(item,":", musica)
    
    pdfRepertorioCreator(repertorio, nomeCliente)
    