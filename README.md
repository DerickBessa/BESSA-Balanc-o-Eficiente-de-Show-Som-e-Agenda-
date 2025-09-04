# B. E. S. S. A. (Balanço Eficiente de Show Som e Agendas)

<h1 align="center">Gerenciamento eficiente de eventos e repertórios ✍️</h1>

##  Sobre o Projeto:

O B.E.S.S.A. é uma ferramenta de linha de comando desenvolvida para otimizar a gestão de eventos, como casamentos católicos e evangélicos. Ele permite um controle completo desde o cadastro inicial do evento até a geração de relatórios detalhados em PDF para os clientes.

O projeto utiliza um banco de dados local SQLite para garantir a persistência e a segurança de todas as informações.

## 🚀 Funcionalidades

* **Criação de Eventos**: Cadastre dados essenciais como nome do cliente, religião, local, valores e datas.

* **Gestão de Repertório**: Organize a trilha sonora de cada momento da cerimônia, associando múltiplas músicas a um único momento.

* **Persistência de Dados**: Armazene todas as informações de eventos e repertórios em um banco de dados local (`clients.db`).

* **Geração de PDFs**: Crie automaticamente resumos de eventos e listas de repertórios em arquivos PDF, salvos em pastas organizadas.

## 💻 Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes tecnologias:

## 🛠️ Estrutura do Projeto

O projeto é modularizado em vários arquivos Python para melhor organização:

* `main.py`: O script principal que inicia a aplicação e guia o usuário através dos processos de criação de eventos e repertórios.

* `bancoDados.py`: Contém todas as funções relacionadas à gestão do banco de dados SQLite, incluindo a criação de tabelas e a inserção de dados.

* `pdfCreator.py`: Contém as funções para gerar os arquivos PDF de repertório e de resumo de evento.

* `dataCreator.py`: Lida com a coleta de informações do evento, como datas, horários e valores, e formata-as.

* `cerimonia.py`: Gerencia a criação do repertório de músicas para a cerimônia, de acordo com o tipo religioso.

* `exibir.py`: Responsável por exibir os cabeçalhos e resumos do evento na tela para o usuário.

## ⚙️ Como Usar

#### Pré-requisitos

Certifique-se de ter o Python instalado. O projeto também usa a biblioteca `fpdf`, que pode ser instalada com o seguinte comando:

pip install fpdf


#### Execução

1. **Repare o Banco de Dados (Opcional):** Se você encontrar problemas com o banco de dados (`clients.db`), execute o script de reparo uma única vez.

python bancoDados.py


Isso irá apagar e recriar as tabelas.

2. **Inicie o Programa Principal:** Execute o arquivo `main.py` para começar a usar o aplicativo.

python main.py


Siga as instruções na tela para inserir os dados do evento e do repertório.

## 📊 GitHub Stats

> **Atenção:** Substitua `DerickBessa` pelo seu próprio nome de usuário do GitHub para ver suas estatísticas.

<br/>

<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/DerickBessa/DerickBessa/output/github-snake-dark.svg" />
<source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/DerickBessa/DerickBessa/output/github-snake.svg" />
<img alt="github-snake" src="https://raw.githubusercontent.com/DerickBessa/DerickBessa/output/github-snake.svg" />
</picture>
