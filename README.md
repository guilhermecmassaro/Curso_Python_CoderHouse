"""
Autor:
Guilherme Crivellenti Massaro

Data da Criação:
14/10/2023

Data da Atualização:
23/11/2023

Versão:
Python 3.11.6

Notas:
Abaixo será apresentado algumas dicas para melhor entendimento do código e sua aplicação

--------------------------------------------------------------------------------------------------------

Documentação: Conexão com APIs e Manipulação de Dados

# Introdução

Este código é um exemplo de um script Python que realiza a conexão com APIs externas para coletar dados e, em seguida, executa algumas operações de manipulação de dados usando a biblioteca Pandas. Além disso, ele demonstra como armazenar os dados em um banco de dados SQLite. Esta documentação fornecerá uma visão geral do código, suas principais funcionalidades e como implementá-lo.

# Bibliotecas utilizadas:

1. Pandas: Para manipulação de dados em formato de tabela.
2. Requests: Para fazer solicitações HTTP e obter dados da API.
3. Plyer: Para notificar o status da conexão com a API.

# Requisitos:

Certifique-se de que as bibliotecas mencionadas no arquivo `requirements.txt` estejam instaladas para executar o script.

# Passo a Passo:

1.	Instale as Bibliotecas:
Certifique-se de ter instaladas as principais bibliotecas acima e todas do arquivo ‘requirements.txt’

2.	Defina as URLs das APIs:
Defina as URLs das APIs externas que você deseja acessar. Substitua as variáveis url_1, url_2 e url_3 pelas URLs reais.

3.	Execução do Script:
Execute o script Python. Ele irá se conectar às APIs, notificar sobre o status da conexão e criar DataFrames com os dados.

4.	Tratamento de Dados (Opcional):
Se desejar, você pode realizar tratamento adicional nos DataFrames, como renomear colunas, converter tipos de dados, preencher valores ausentes, etc.

6.	Armazenamento em Banco de Dados:
O código inclui uma função salvar_base_de_dados que permite salvar os DataFrames em um banco de dados SQLite. Certifique-se de definir o nome do banco de dados desejado e a tabela em que deseja armazenar os dados do dataframe colocado.
