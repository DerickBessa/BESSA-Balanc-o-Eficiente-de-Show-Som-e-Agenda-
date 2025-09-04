B. E. S. S. A. (Balanço Eficiente de Show Som e Agendas)
Visão Geral
O B.E.S.S.A. é uma ferramenta de linha de comando desenvolvida para auxiliar na gestão de eventos, como casamentos católicos e evangélicos. Ele permite que você cadastre informações detalhadas sobre cada evento, crie repertórios de música personalizados e gere relatórios em PDF para clientes.

O projeto utiliza um banco de dados SQLite para armazenar as informações de forma persistente.

Funcionalidades
Criação de Eventos: Cadastre dados essenciais como nome do cliente, religião, local, valores e datas.

Gestão de Repertório: Organize a trilha sonora de cada momento da cerimônia, com a possibilidade de associar várias músicas a um mesmo momento.

Persistência de Dados: Armazene todas as informações de eventos e repertórios em um banco de dados local (clients.db).

Geração de PDFs: Crie automaticamente resumos de eventos e listas de repertórios em arquivos PDF, salvos em pastas organizadas.

Como Usar
Pré-requisitos
Certifique-se de ter o Python instalado. O projeto também usa a biblioteca fpdf, que pode ser instalada com o seguinte comando:

pip install fpdf

Execução
Repare o Banco de Dados (Opcional): Se você encontrar problemas com o banco de dados (clients.db), execute o script de reparo uma única vez.

python bancoDados.py

Isso irá apagar e recriar as tabelas.

Inicie o Programa Principal: Execute o arquivo main.py para começar a usar o aplicativo.

python main.py

Siga as instruções na tela para inserir os dados do evento e do repertório.

Estrutura do Projeto
O projeto é modularizado em vários arquivos Python para melhor organização:

main.py: O script principal que inicia a aplicação e guia o usuário através dos processos de criação de eventos e repertórios.

bancoDados.py: Contém todas as funções relacionadas à gestão do banco de dados SQLite, incluindo a criação de tabelas e a inserção de dados.

pdfCreator.py: Contém as funções para gerar os arquivos PDF de repertório e de resumo de evento.

dataCreator.py: Lida com a coleta de informações do evento, como datas, horários e valores, e formata-as.

cerimonia.py: Gerencia a criação do repertório de músicas para a cerimônia, de acordo com o tipo religioso.

exibir.py: Responsável por exibir os cabeçalhos e resumos do evento na tela para o usuário.

Banco de Dados
O banco de dados clients.db utiliza duas tabelas para armazenar as informações:

eventos: Armazena os dados gerais de cada evento.

id (INTEGER PRIMARY KEY)

nomeCliente (TEXT)

religiao (TEXT)

valor_total (REAL)

entrada (REAL)

entrada_paga (TEXT)

local (TEXT)

data_inicio (TEXT)

data_fim (TEXT)

duracao (TEXT)

repertorio: Armazena as músicas de cada evento, vinculadas pelo ID do evento.

id (INTEGER PRIMARY KEY)

evento_id (INTEGER)

momento (TEXT)

musica (TEXT)

Geração de PDFs
Todos os PDFs gerados são salvos em um diretório PDF na mesma pasta do projeto, com subdiretórios para Repertorios e Eventos, para manter a organização dos arquivos de saída.
