# Importando as bibliotecas necessárias

import pandas as pd
import requests
from plyer import notification
import sqlite3

# Realizando a conexão com as três diferentes e armazenando os dados em variáveis

def fazer_requisicao_e_notificar(url, tabela): # função destinada a conectar na url desejada e retornar o json
    response = requests.get(url)
    if response.status_code == 200:
        notification.notify(title='Conexão com API', message=f'Conexão realizada com sucesso na Tabela {tabela}')
        print(f'Conexão realizada com sucesso na Tabela {tabela}')
        return response.json()
    else:
        notification.notify(title='Conexão com API', message=f'Conexão não realizada na Tabela {tabela}')
        print(f'Erro na Tabela {tabela} com código {response.status_code}')
        return None

url_1 = 'https://brasilapi.com.br/api/banks/v1'
url_2 = 'https://brasilapi.com.br/api/cvm/corretoras/v1'
url_3 = 'https://brasilapi.com.br/api/cptec/v1/clima/capital'

# Fazendo as requisições com a função necessária e armazenando os dados em variáveis

bancos = fazer_requisicao_e_notificar(url_1, 1) 
corretoras = fazer_requisicao_e_notificar(url_2, 2)
climas = fazer_requisicao_e_notificar(url_3, 3)

# Transformando os dicionários (json) em dataframes

df_bancos = pd.DataFrame(bancos)
df_corretoras = pd.DataFrame(corretoras)
df_climas = pd.DataFrame(climas)

# Alterando os nomes da colunas para melhor entendimento e tratamento dos dados

df_bancos.columns = ['Ispb','Nome Abreviado','Codigo','Nome Completo']
df_corretoras.columns = ['CNPJ','Tipo','Razão Social','Nome Comercial','Status','E-mail','Telefone','CEP','Pais','UF','Municipio','Bairro','Complemento','Logradouro','Data Patrimonio Liquido','Valor Liq Patrimonio','CVM','Data Inicio Situacao','Data Registro']
df_climas.columns = ['Umidade','Intensidade','Codigo ICAO','Pressao Atmosferica','Velocidade Vento','Direcao Vento','Condicao','Descricao Condicao','Temperatura','Atualizacao']

# Tratamento de missing values na base de Bancos

df_bancos = df_bancos.fillna({
    'Nome Abreviado' : '-',
    'Codigo' : 0,
    'Nome Completo' : '-'
})

df_bancos['Codigo'] = df_bancos['Codigo'].astype(int).astype(object) # Converte para inteiro para retirar os decimais e ai coloca os codigos em formato de texto pois eles não são somáveis

# Tratamento de Datas na base de Corretoras

df_corretoras['Data Patrimonio Liquido'] = pd.to_datetime(df_corretoras['Data Patrimonio Liquido'])
df_corretoras['Data Inicio Situacao'] = pd.to_datetime(df_corretoras['Data Inicio Situacao'])
df_corretoras['Data Registro'] = pd.to_datetime(df_corretoras['Data Registro'])

# Tratanmento das Datas e Decimais na base de Climas

df_climas = df_climas.astype({'Umidade' : 'float',
                  'Pressao Atmosferica' : 'float',
                  'Velocidade Vento' : 'float',
                  'Direcao Vento' : 'float',
                  'Temperatura' : 'float'})

df_climas['Atualizacao'] = pd.to_datetime(df_climas['Atualizacao'])

# Criação de modelos Stack e Unstack para as colunas tratadas acima

# Tabela da API de Bancos
df_bancos_index = df_bancos.set_index('Ispb',append=True) # Cria um index para as colunas
df_bancos_stack = df_bancos_index.stack() # Realiza o stack da tabela de index
df_bancos_unstack = df_bancos_stack.unstack() # Realiza o unstack da tabela de stack

# Tabela da API de Corretoras
df_corretoras_index = df_corretoras.set_index(['CNPJ','Tipo'],append=True) # Cria um index para as colunas
df_corretoras_stack = df_corretoras_index.stack() # Realiza o stack da tabela de index
df_corretoras_unstack = df_corretoras_stack.unstack() # Realiza o unstack da tabela de stack

# Tabela da API de Climas
df_climas_index = df_climas.set_index(['Codigo ICAO','Descricao Condicao'],append=True) # Cria um index para as colunas
df_climas_stack = df_climas_index.stack() # Realiza o stack da tabela de index
df_climas_unstack = df_climas_stack.unstack() # Realiza o unstack da tabela de stack

# Função para salvar o Dataframe com seu respectivo nome de tabela no banco de dados escolhido
def salvar_base_de_dados(df, nome_tabela,banco_de_dados):
    conn = sqlite3.connect(banco_de_dados)
    df.to_sql(f'{nome_tabela}', conn, if_exists='replace',index=False)
    conn.close()

df_corretoras_compactada = df_corretoras[['CNPJ','Tipo','Valor Liq Patrimonio']] # Por problemas de tamanho, foi realizado uma compactação do dataframe da API de corretoras

# Salvando as bases de dados tratadas no respectivo banco de dados

salvar_base_de_dados(df_bancos,'Bancos','coderhouse.db')
salvar_base_de_dados(df_climas,'Climas','coderhouse.db')
salvar_base_de_dados(df_corretoras_compactada,'Corretoras','coderhouse.db')



