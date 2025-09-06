import requests
import psycopg2
from db_config import DB_CONFIG

def fetch_data_from_api():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=01/01/2010&dataFinal=31/12/2016"
    response = requests.get(url)
    return response.json()  # Ok, pois formato=json

def insert_data_to_db(data):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    for item in data:
        # Converte data para yyyy-mm-dd se necessário
        # Converte valor para float (troca vírgula por ponto)
        dia = item['data']  # ou ajuste conforme necessário
        valor = item['valor'].replace(',', '.')
        cursor.execute(
            "INSERT INTO tb_taxa_selic (dia, valor) VALUES (%s, %s)", 
            (dia, valor)
        )
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    dados = fetch_data_from_api()
    insert_data_to_db(dados)