# main_script.py (seu arquivo)
from Creators.dataCreator import criarDataEvento 
from view.exibir import cabecalhoFinalizar, cabecalhoIniciar, cabecalhoDefault, cabecalhoReinicio
from Creators.cerimonia import cerimoniaCreator, exibirRepertorio
from datetime import date, datetime, timedelta
from BancoDeDados.bancoDados import criar_tabelas, inserir_evento
from Creators.excelCreator import salvar_evento_excel, editar_evento_excel
import os

def main():
    criar_tabelas()
    lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                   "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    while True:  # loop que permite repetir o processo quantas vezes quiser
        os.system('cls' if os.name == "nt" else 'clear')
        cabecalhoDefault()
        start = input("| Deseja criar uma data? (S/N):  ").strip().upper()
        if start == 'S':
            os.system('cls' if os.name == "nt" else 'clear')
            cabecalhoIniciar("E")
            nomeCliente = input("Qual o nome do contratante? ").upper()
            nomeCliente, resumo_evento, yearEvent, monthEvent = criarDataEvento(nomeCliente)
            inserir_evento(resumo_evento)
            monthEvent = lista_meses[(monthEvent - 1)]
            salvar_evento_excel(f"{monthEvent}_{yearEvent}", resumo_evento)
            os.system('cls' if os.name == "nt" else 'clear')

            # esta função agora retorna a escolha do usuário (ex: 'F' para reiniciar)
            escolha = cabecalhoReinicio()
            if escolha == 'F':
                continue
            else:
                cabecalhoFinalizar("E")
                break  # sai do while e finaliza o programa
        elif start == "N":
            os.system('cls' if os.name == "nt" else 'clear')
            cabecalhoDefault()
            edit_start= input("Voce deseja editar um EVENTO? (S/N):  ").upper()
            if edit_start == "S":
                nome_arquivo_editar = input("Qual data gostaria de editar?(MM/YYYY): ")
                nome_arquivo_editar= nome_arquivo_editar.split("/")
                nome_arquivo_editar[0]= lista_meses[int(nome_arquivo_editar[0])- 1]
                arquivo_editar = f"{nome_arquivo_editar[0]}_{nome_arquivo_editar[1]}.xlsx"
                editar_evento_excel(arquivo_editar)
            else:
                cabecalhoFinalizar("E")
                break
        else:
            cabecalhoFinalizar("E")
            break

if __name__ == "__main__":
    main()
