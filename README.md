# B. E. S. S. A.

## Visão Geral

O B.E.S.S.A. (Balanço Eficiente de Show Som e Agendas) é uma ferramenta de linha de comando desenvolvida para gerenciar eventos como casamentos. O projeto permite cadastrar informações detalhadas sobre os eventos e os repertórios de música.

Os dados são armazenados em um banco de dados local SQLite, e é possível gerar relatórios em PDF para clientes.

## Funcionalidades

* Criação e cadastro de eventos com dados como cliente, local, datas e valores.

* Gerenciamento de repertórios musicais por momento da cerimônia.

* Geração de PDFs de resumo do evento e do repertório.

* Persistência dos dados em um banco de dados local.

## Estrutura do Projeto

O projeto é dividido em módulos:

* `main.py`: O script principal que inicia a aplicação.

* `bancoDados.py`: Gerencia a conexão com o banco de dados e as operações de inserção.

* `pdfCreator.py`: Responsável por gerar os arquivos PDF.

* `dataCreator.py`: Coleta e formata os dados do evento.

* `cerimonia.py`: Gerencia a criação do repertório.

* `exibir.py`: Exibe as informações do evento na tela.

## Como Usar

### Pré-requisitos

Certifique-se de ter o Python instalado. Instale a biblioteca `fpdf`:

pip install fpdf


### Execução

1. Se o banco de dados estiver corrompido, execute o script de reparo uma vez:

python bancoDados.py


2. Para iniciar o programa, execute o `main.py`:

python main.py


Siga as instruções no terminal para criar um novo evento.
