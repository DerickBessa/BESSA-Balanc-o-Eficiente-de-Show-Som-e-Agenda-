import sqlite3

DB_name = "clients.db"

def conectar_db():
    """Conecta-se ao banco de dados."""
    return sqlite3.connect(DB_name)

def criar_tabelas():
    """Cria as tabelas eventos e repertorio."""
    conn = conectar_db()
    cursor = conn.cursor()

    # Tabela de eventos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeCliente TEXT NOT NULL,
            religiao TEXT,
            valor_total REAL,
            entrada REAL,
            entrada_paga TEXT,
            local TEXT,
            data_inicio TEXT,
            data_fim TEXT,
            data_pagamento_resto TEXT,
            duracao TEXT,
            custo_total REAL,
            lucro_total REAL
        )
    """)

    # Tabela de repertório
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repertorio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            evento_id INTEGER,
            momento TEXT,
            musica TEXT,
            FOREIGN KEY(evento_id) REFERENCES eventos(id)
        )
    """)

    conn.commit()
    conn.close()

def inserir_evento(resumo_evento):
    """Insere um novo evento na tabela eventos. Retorna o ID do evento inserido."""
    conn = conectar_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO eventos (
            nomeCliente, religiao, valor_total, entrada, entrada_paga, local, 
            data_inicio, data_fim, data_pagamento_resto, duracao, custo_total, lucro_total
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        resumo_evento["Cliente"],
        resumo_evento["Religião"],
        resumo_evento["Valor total"],
        resumo_evento["Entrada valor"],
        resumo_evento["Entrada situacao"],
        resumo_evento["Local"],
        resumo_evento["Início"],
        resumo_evento["Fim"],
        resumo_evento["Data pagamento faltante"],
        resumo_evento["Duração"],
        resumo_evento["Custo"],
        resumo_evento["Lucro"],
    ))

    conn.commit()
    evento_id = cursor.lastrowid
    conn.close()
    return evento_id

def inserir_repertorio(evento_id, repertorio):
    """Insere o repertório de músicas na tabela repertorio para um evento específico."""
    conn = conectar_db()
    cursor = conn.cursor()

    for momento, musicas in repertorio.items():
        for musica in musicas:
            cursor.execute("""
                INSERT INTO repertorio (evento_id, momento, musica)
                VALUES (?, ?, ?)
            """, (evento_id, momento, musica))

    conn.commit()
    conn.close()
    print("Repertório inserido com sucesso.")

def reparar_e_criar_db():
    """
    Restaura o banco de dados para um estado limpo.
    1. Exclui as tabelas existentes.
    2. Recria as tabelas eventos e repertorio.
    """
    conn = conectar_db()
    cursor = conn.cursor()

    # Deleta as tabelas para garantir um estado limpo
    cursor.execute("DROP TABLE IF EXISTS repertorio")
    cursor.execute("DROP TABLE IF EXISTS eventos")

    conn.commit()
    conn.close()

    # Recria as tabelas
    criar_tabelas()
    print("Banco de dados reparado com sucesso!")
    print("As tabelas 'eventos' e 'repertorio' foram recriadas.")
    print("Você pode agora rodar o seu script principal (main.py) para popular os dados.")

def limpar_duplicados():
    """Remove registros duplicados das tabelas eventos e repertorio, mantendo o menor ID."""
    conn = conectar_db()
    cursor = conn.cursor()

    # Apagar duplicados em eventos, mantendo o menor ID
    cursor.execute("""
        DELETE FROM eventos
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM eventos
            GROUP BY nomeCliente, religiao, valor_total, entrada, entrada_paga, local, 
                     data_inicio, data_fim, data_pagamento_resto, duracao, custo_total, lucro_total
        )
    """)

    # Apagar duplicados em repertorio, mantendo o menor ID
    cursor.execute("""
        DELETE FROM repertorio
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM repertorio
            GROUP BY evento_id, momento, musica
        )
    """)

    # Não resetamos IDs para não bagunçar a sequência
    conn.commit()
    conn.close()
    print("Duplicados removidos com sucesso! IDs existentes permanecem intactos.")

# Executa a função de reparo ao rodar diretamente
if __name__ == "__main__":
    reparar_e_criar_db()
