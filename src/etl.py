# Script principal do pipeline ETL usando psycopg2
import psycopg2
import pandas as pd
from db_config import DB_CONFIG

# Conecta ao banco de dados PostgreSQL
conn = psycopg2.connect(**DB_CONFIG)
cursor = conn.cursor()

# Seleciona os 1000 primeiros registros da tabela tb_taxa_selic
query = "SELECT * FROM tb_taxa_selic"
cursor.execute(query)
rows = cursor.fetchall()

# Obtém os nomes das colunas
colnames = [desc[0] for desc in cursor.description]

# Cria um DataFrame pandas com os dados
df_top1000 = pd.DataFrame(rows, columns=colnames)

# Salva o DataFrame em CSV
df_top1000.to_csv("./output/txa_selic.csv", index=False)

def salvar_excel(df, caminho_arquivo):
    """
    Salva o DataFrame como arquivo Excel (.xlsx)
    """
    df.to_excel(caminho_arquivo, index=False)

# Exemplo de uso após criar o DataFrame:
salvar_excel(df_top1000, "./output/top1000.xlsx")

cursor.close()