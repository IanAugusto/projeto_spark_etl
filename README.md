# Projeto ETL - Taxa Selic

Este projeto realiza a extração, transformação e carga (ETL) dos dados da Taxa Selic, utilizando Python, PostgreSQL e Pandas. Os dados são obtidos diretamente da API do Banco Central, armazenados em banco de dados e exportados para arquivos CSV e Excel.

## Estrutura de Pastas

```
projeto_spark_etl/
├── data/                # (Opcional) Pasta para dados simulados
├── src/
│   ├── etl.py           # Pipeline principal: consulta e exportação dos dados
│   └── api_db.py        # Script para buscar dados da API e inserir no banco
│   └── utils.py         # Funções auxiliares
├── output/              # Dados processados e relatórios gerados
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
```

## Fluxo do Projeto

1. **Coleta de Dados**
   - O script `src/api_db.py` acessa a [API do Banco Central](https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json) e insere os dados na tabela `tb_taxa_selic` do PostgreSQL.

2. **Processamento e Exportação**
   - O script `src/etl.py` conecta ao banco, seleciona os dados da tabela e exporta para arquivos CSV e Excel na pasta `output/`.

## Como Executar

### 1. Preparação do Ambiente

Crie e ative um ambiente virtual:
```powershell
python -m venv env
.\env\Scripts\Activate
```

Instale as dependências:
```powershell
pip install -r requirements.txt
```

### 2. Configuração do Banco de Dados

- Crie um banco PostgreSQL local.
- Crie a tabela `tb_taxa_selic`:
  ```sql
  CREATE TABLE tb_taxa_selic (
      id_info SERIAL PRIMARY KEY,
      dia DATE,
      valor NUMERIC
  );
  ```
- Configure o arquivo `src/db_config.py` com suas credenciais de acesso.

### 3. Coleta e Inserção dos Dados

Execute o script para buscar e inserir os dados da API:
```powershell
python src/api_db.py
```

### 4. Exportação dos Dados

Execute o pipeline ETL para exportar os dados:
```powershell
python src/etl.py
```

Os arquivos gerados estarão na pasta `output/`.

## Observações

- O projeto utiliza apenas Pandas e Psycopg2 para manipulação dos dados.
- O uso do Spark está planejado para versões futuras.
- Para exportar em Excel, o Pandas precisa do pacote `openpyxl` instalado.

## Dependências Principais

- pandas
- psycopg2-binary
- requests
- openpyxl (para exportação Excel)

## Autor

Projeto desenvolvido por Ian Augusto Alvarenga Tonim.
