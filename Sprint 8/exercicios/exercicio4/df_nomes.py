from pyspark.sql import SparkSession
from pyspark import SparkContext, SQLContext
from pyspark.sql.functions import expr, when, rand, lit, concat_ws, to_date, year, col


# Inicialize a Spark Session
spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()

# Leia o arquivo nomes_aleatorios.txt
caminho = "/content/drive/MyDrive/Colab Notebooks/exercicio4/nomes_aleatorios.txt"
df_nomes = spark.read.csv(caminho, header=False)

# Mostre algumas linhas do dataframe (por exemplo, as 5 primeiras linhas)
df_nomes.show(5)

# Renomeie a coluna "_c0" para "Nomes"
df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")

# Mostre as 5 primeiras linhas após a renomeação
df_nomes.show(10)

valores_escolaridade = ["Fundamental", "Medio", "Superior"]

# Adicione a coluna "Escolaridade" com valores aleatórios
df_nomes = df_nomes.withColumn("Escolaridade", expr("CASE WHEN rand() < 1/3 THEN 'Fundamental' WHEN rand() < 2/3 THEN 'Medio' ELSE 'Superior' END"))

# Mostre 10 linhas do dataframe com a coluna "Escolaridade" adicionada
df_nomes.show(10)

## Crie uma lista com os 13 países da América do Sul
paises_america_sul = ['Brasil', 'Argentina', 'Chile', 'Colômbia', 'Peru', 'Venezuela', 'Equador', 'Bolívia', 'Paraguai', 'Uruguai', 'Guiana', 'Suriname', 'Guiana Francesa']

# Adicione uma nova coluna "Pais" com valores aleatórios da lista de países
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

# Mostrar o DataFrame resultante
df_nomes.show(10)

# Adicione a coluna "AnoNascimento" com anos aleatórios no século XX
df_nomes = df_nomes.withColumn("AnoNascimento", (lit(1945) + (rand() * (2010 - 1945 + 1)).cast("int")))

# Mostre 10 linhas do dataframe com a coluna "AnoNascimento" adicionada
df_nomes.show(10)

# Converta o campo "AnoNascimento" em uma data válida, considerando o primeiro dia do ano
df_nomes = df_nomes.withColumn("DataNascimento", to_date(concat_ws("-", col("AnoNascimento"), lit("01"), lit("01")), "yyyy-MM-dd"))

# Selecione as pessoas que nasceram neste século (a partir de 2000)
df_select = df_nomes.filter(year("DataNascimento") >= 2000)

# Mostre os 10 primeiros nomes e suas respectivas datas de nascimento
df_select.select("Nomes", "DataNascimento").show(10)

# Filtrar as pessoas da geração Millennials (nascidos entre 1980 e 1994)
millennials_count_df = df_nomes.filter((year("DataNascimento") >= 1980) & (year("DataNascimento") <= 1994))

# Conte o número de pessoas da geração Millennials
millennials_count = millennials_count_df.count()

# Mostre o resultado em um novo DataFrame
result_df = spark.createDataFrame([(millennials_count,)], ["Count"])

millennials_count = df_nomes.select("DataNascimento")\
    .filter((year("DataNascimento") >= 1980) & (year("DataNascimento") <= 1994))\
    .count()

# Exiba o número de pessoas da geração Millennials
millennials_count

query = """
SELECT COUNT(*) AS MillennialsCount
FROM pessoas
WHERE year(DataNascimento) >= 1980 AND year(DataNascimento) <= 1994
"""

millennials_count_df = spark.sql(query)

# Exiba o resultado
millennials_count = millennials_count_df.first().MillennialsCount
millennials_count

