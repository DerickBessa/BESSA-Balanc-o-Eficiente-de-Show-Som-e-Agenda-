# 🎵 B.E.S.S.A.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQLite3](https://img.shields.io/badge/SQLite-3.39.5-orange?logo=sqlite)
![DB Browser](https://img.shields.io/badge/DB_Browser-3.12.2-lightgrey?logo=sqlite)


## Visão Geral

**B.E.S.S.A.** (*Balanço Eficiente de Show, Som e Agendas*) é uma ferramenta de **linha de comando** desenvolvida para gerenciar eventos, como casamentos.  

O projeto permite cadastrar informações detalhadas sobre os eventos e os repertórios de música, armazenando tudo em um banco de dados local **SQLite**. Também é possível gerar relatórios em **PDF** para os clientes.

---

## Funcionalidades

- ✅ Cadastro de eventos com informações detalhadas: cliente, local, datas e valores.  
- ✅ Gerenciamento de repertórios musicais por momento da cerimônia.  
- ✅ Geração de PDFs resumindo o evento e o repertório.  
- ✅ Persistência dos dados em banco de dados local.

---

## Estrutura do Projeto

O projeto é modularizado em arquivos Python para melhor organização:

| Arquivo           | Função                                                                 |
|------------------|------------------------------------------------------------------------|
| `main.py`        | Script principal que inicia a aplicação.                               |
| `bancoDados.py`  | Gerencia a conexão com o banco e operações de inserção.                |
| `pdfCreator.py`  | Gera arquivos PDF de repertório e resumo de evento.                   |
| `dataCreator.py` | Coleta e formata dados do evento.                                      |
| `cerimonia.py`   | Gerencia a criação do repertório de acordo com o tipo de cerimônia.    |
| `exibir.py`      | Exibe informações do evento na tela.                                   |

---

## Banco de Dados

O banco de dados `clients.db` possui duas tabelas:

### **eventos**
Armazena os dados gerais de cada evento.

| Coluna          | Tipo    |
|----------------|---------|
| id              | INTEGER PRIMARY KEY |
| nomeCliente     | TEXT    |
| religiao        | TEXT    |
| valor_total     | REAL    |
| entrada         | REAL    |
| entrada_paga    | TEXT    |
| local           | TEXT    |
| data_inicio     | TEXT    |
| data_fim        | TEXT    |
| duracao         | TEXT    |

### **repertorio**
Armazena as músicas de cada evento, vinculadas pelo ID do evento.

| Coluna       | Tipo    |
|-------------|---------|
| id           | INTEGER PRIMARY KEY |
| evento_id    | INTEGER |
| momento      | TEXT    |
| musica       | TEXT    |

---

## Como Usar

### Pré-requisitos

- Python 3.x instalado.  
- Biblioteca `fpdf` instalada:

```bash
pip install fpdf
```

  
- Todos os títulos (`##` ou `###`) estão corretos.  
- Todos os blocos de código estão fechados.  
- Listas estão corretamente renderizadas.  
- Quebras de linha e separadores `---` garantem boa leitura no GitHub.  

## Geração de PDFs

Todos os PDFs são salvos em um diretório `PDF` dentro da pasta do projeto, com subdiretórios separados para:

- **Repertórios**
- **Eventos**

Isso mantém os arquivos organizados e de fácil acesso.

---

## Conclusão

O **B.E.S.S.A.** oferece uma solução simples, eficiente e organizada para o gerenciamento de eventos e repertórios musicais, permitindo que você tenha controle completo sobre cada detalhe do evento e gere relatórios profissionais para os clientes.

