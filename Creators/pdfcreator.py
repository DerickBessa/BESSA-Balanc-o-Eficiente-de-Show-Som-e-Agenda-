from fpdf import FPDF
import os

def pdfRepertorioCreator(repertorio, nomeCliente):
    pdf = FPDF()
    pdf.add_page()
    
    # Título centralizado
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"REPERTÓRIO ATUAL DE {nomeCliente}", ln=True, align="C")
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 12, "Momento", border=1, align="C")
    pdf.cell(110, 12, "Música", border=1, align="C")
    pdf.ln()

    # Conteúdo da tabela
    for item, musica in repertorio.items():
        # Nome do momento em bold e centralizado
        pdf.set_font("Arial", "B", 12)
        pdf.cell(80, 15, str(item), border=1, align="C")

        # Música em bold e centralizado
        pdf.set_font("Arial", "B", 12)
        if isinstance(musica, list):
            musica_texto = ", ".join(musica)
        else:
            musica_texto = str(musica)
        pdf.cell(110, 15, musica_texto, border=1, align="C")
        pdf.ln()

    # Salvar PDF
    diretorio_eventos = os.path.join(os.getcwd(),"PDF", "Repertorios")  # cria caminho absoluto
    os.makedirs(diretorio_eventos, exist_ok=True)  # cria a pasta se não existir
    
    arquivo = f"{nomeCliente.lower().replace(' ', '_')}_repertorio.pdf"
    caminho_completo = os.path.join(diretorio_eventos, arquivo)

    pdf.output(caminho_completo)
    print(f"PDF criado com sucesso: {caminho_completo}")

def pdfEventCreator(repertorio,nomeCliente):

    pdf = FPDF()
    pdf.add_page()
    
    # Título centralizado
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"EVENTO DE {nomeCliente}", ln=True, align="C")
    pdf.ln(10)

    # Cabeçalho da tabela
    pdf.set_font("Arial", "B", 12)
    pdf.cell(190, 12, f"DADOS DO EVENTO", border=1, align="C")
    
    pdf.ln()

    # Conteúdo da tabela
    for dado, evento in repertorio.items():
        # Nome do momento em bold e centralizado
        pdf.set_font("Arial", "B", 12)
        pdf.cell(80, 15, str(dado), border=1, align="C")

        # Música em bold e centralizado
        pdf.set_font("Arial", "B", 12)
        if isinstance(evento, list):
            musica_texto = ", ".join(evento)
        else:
            musica_texto = str(evento)
        pdf.cell(110, 15, musica_texto, border=1, align="C")
        pdf.ln()

    # Salvar PDF
    diretorio_repertorios= os.path.join(os.getcwd(),"PDF",  "Eventos")  # cria caminho absoluto
    os.makedirs(diretorio_repertorios, exist_ok=True)  # cria a pasta se não existir
    
    arquivo = f"{nomeCliente.lower().replace(' ', '_')}_evento.pdf"
    caminho_completo = os.path.join(diretorio_repertorios, arquivo)

    pdf.output(caminho_completo)
    print(f"PDF criado com sucesso: {caminho_completo}")