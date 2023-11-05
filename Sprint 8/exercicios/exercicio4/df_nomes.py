from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import expr, when, rand, lit, concat_ws, to_date, year, col


# Inicializando a Spark Session
spark = SparkSession.builder.master(
    "local[*]").appName("Exercicio Intro").getOrCreate()

caminho = "/nomes_aleatorios.txt"
df_nomes = spark.read.csv(caminho, header=False)

df_nomes.show(5)

# Renomeando a coluna "_c0" para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

df_nomes.show(10)

valores_escolaridade = ["Fundamental", "Medio", "Superior"]

# Adicionando a coluna "Escolaridade" com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", expr(
    "CASE WHEN rand() < 1/3 THEN 'Fundamental' WHEN rand() < 2/3 THEN 'Medio' ELSE 'Superior' END"))

df_nomes.show(10)

# Criando uma lista com os 13 países da América do Sul
paises_america_sul = ['Brasil', 'Argentina', 'Chile', 'Colômbia', 'Peru', 'Venezuela',
                      'Equador', 'Bolívia', 'Paraguai', 'Uruguai', 'Guiana', 'Suriname', 'Guiana Francesa']

# Adicionando uma nova coluna "Pais" com valores aleatórios da lista de países
df_nomes = df_nomes.withColumn("Pais", when(rand() <= 1/13, lit(paises_america_sul[0]))
                               .when(rand() <= 2/13, lit(paises_america_sul[1]))
                               .when(rand() <= 3/13, lit(paises_america_sul[2]))
                               .when(rand() <= 4/13, lit(paises_america_sul[3]))
                               .when(rand() <= 5/13, lit(paises_america_sul[4]))
                               .when(rand() <= 6/13, lit(paises_america_sul[5]))
                               .when(rand() <= 7/13, lit(paises_america_sul[6]))
                               .when(rand() <= 8/13, lit(paises_america_sul[7]))
                               .when(rand() <= 9/13, lit(paises_america_sul[8]))
                               .when(rand() <= 10/13, lit(paises_america_sul[9]))
                               .when(rand() <= 11/13, lit(paises_america_sul[10]))
                               .when(rand() <= 12/13, lit(paises_america_sul[11]))
                               .otherwise(lit(paises_america_sul[12])))

df_nomes.show(10)

# Adicionando a coluna "AnoNascimento" com anos aleatórios no século XX
df_nomes = df_nomes.withColumn("AnoNascimento", (lit(
    1945) + (rand() * (2010 - 1945 + 1)).cast("int")))

df_nomes.show(10)

# Convertendo o campo "AnoNascimento" em uma data válida, considerando o primeiro dia do ano
df_nomes = df_nomes.withColumn("DataNascimento", to_date(
    concat_ws("-", col("AnoNascimento"), lit("01"), lit("01")), "yyyy-MM-dd"))

# Selecione as pessoas que nasceram neste século (a partir de 2000)
df_select = df_nomes.filter(year("DataNascimento") >= 2000)

# Mostrando os 10 primeiros nomes e suas respectivas datas de nascimento
df_select.select("Nomes", "DataNascimento").show(10)

# Registrando o DataFrame df_nomes como uma tabela temporária
df_nomes.createOrReplaceTempView("pessoas")

# Executando uma consulta Spark SQL para selecionar as pessoas que nasceram neste século (a partir de 2000)
query = """
    SELECT Nomes, DataNascimento
    FROM pessoas
    WHERE year(DataNascimento) >= 2000
    LIMIT 10
"""

df_result = spark.sql(query)

df_result.show()

# Filtrando as pessoas da geração Millennials (nascidas entre 1980 e 1994)
millennials_count_df = df_nomes.filter(
    (year("DataNascimento") >= 1980) & (year("DataNascimento") <= 1994))

# Contando o número de pessoas da geração Millennials
millennials_count = millennials_count_df.count()

print(millennials_count)

# Executando a consulta Spark SQL
query = """
    SELECT COUNT(*) AS MillennialsCount
    FROM df_nomes
    WHERE year(DataNascimento) >= 1980 AND year(DataNascimento) <= 1994
"""

millennials_count_df = spark.sql(query)

# Obtendo o resultado da contagem
millennials_count = millennials_count_df.first().MillennialsCount

print(millennials_count)

df_nomes.createOrReplaceTempView("pessoas")

# Executando uma consulta Spark SQL para contar o número de pessoas por país e geração
query = """
SELECT Pais,
       CASE
           WHEN year(DataNascimento) BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
           WHEN year(DataNascimento) BETWEEN 1965 AND 1979 THEN 'Geração X'
           WHEN year(DataNascimento) BETWEEN 1980 AND 1994 THEN 'Millennials'
           WHEN year(DataNascimento) BETWEEN 1995 AND 2015 THEN 'Geração Z'
           ELSE 'Outra Geração'
       END AS Geracao,
       COUNT(*) AS Quantidade
FROM pessoas
GROUP BY Pais, Geracao
"""

result_df = spark.sql(query)

# Ordenenando o DataFrame em ordem crescente de Pais, Geracao e Quantidade
result_df = result_df.orderBy("Pais", "Geracao", "Quantidade")

result_df.show()

# Finalizando a Spark Session
spark.stop()
