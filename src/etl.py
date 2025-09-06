# Script principal do pipeline ETL
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ETL_Pipeline")
    .config("spark.jars", "jars/postgresql-42.7.7.jar")  # <-- Adicione o caminho do JAR aqui
    .getOrCreate()
)

df = (
    spark.read
    .format("jdbc")
    .option("url", "jdbc:postgresql://localhost:5432/postgres")
    .option("dbtable", "tb_taxa_selic")
    .option("user", "postgres")
    .option("password", "123456")
    .option("driver", "org.postgresql.Driver") 
    .load()
)

# Transformações Spark
df_clean = df.dropna()
df_clean.write.csv("../output/dados_final.csv", header=True, mode="overwrite")
spark.stop()