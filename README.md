# Projeto Spark ETL

Pipeline de ETL distribuído utilizando PySpark e PostgreSQL

Este projeto está em desenvolvimento e visa demonstrar como construir uma rotina ETL (Extract, Transform, Load) utilizando PySpark para processar dados de um banco PostgreSQL, realizar transformações e exportar os resultados em formato CSV.

## Objetivos

- Integrar o Spark, via PySpark, com bancos de dados relacionais utilizando JDBC.
- Aplicar transformações de dados (como limpeza, filtragem e manipulação) de forma distribuída.
- Salvar os dados processados em arquivos para análise ou integração com outras ferramentas.
- Documentar o processo de configuração do ambiente, incluindo dependências específicas para Windows.

## Tecnologias Utilizadas

- **Python 3.10+**
- **PySpark**
- **PostgreSQL**
- **JDBC Driver (PostgreSQL)**
- **winutils.exe** (necessário para rodar Spark em ambientes Windows)

## Estrutura do Projeto

- `src/etl.py` — Script principal do pipeline ETL.
- `src/api_db.py` — Funções de integração com o banco de dados.
- `output/` — Pasta destino dos arquivos gerados (CSV).
- `jars/` — Drivers JDBC necessários para comunicação com o banco.
- `.venv/` — Ambiente virtual Python para gerenciamento de dependências.

## Status do Projeto

**Este projeto ainda está em desenvolvimento e não está finalizado.**
Algumas funcionalidades e documentações podem sofrer alterações ou aprimoramentos ao longo do tempo.

## Como executar

1. Instale as dependências Python com `pip install -r requirements.txt`
2. Baixe e configure o driver JDBC do PostgreSQL em `jars/`
3. (Windows) Baixe e configure o `winutils.exe` em `C:\hadoop\bin`
4. Ajuste as configurações de conexão com o banco em `src/api_db.py`
5. Execute o pipeline:
    ```
    python src/etl.py
    ```

## Próximos passos

- Adicionar testes automatizados
- Melhorar tratamento de erros e validações
- Documentação detalhada das etapas do ETL
- Exemplos de transformações mais avançadas
- Suporte para outros bancos ou formatos de saída

---

Se tiver sugestões ou encontrar problemas, fique à vontade para abrir uma issue ou contribuir!
