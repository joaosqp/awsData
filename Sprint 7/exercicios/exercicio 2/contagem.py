from pyspark.sql import SparkSession

# Iniciando uma sessão Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# URL do arquivo README.md no GitHub
url = "https://raw.githubusercontent.com/joaosqp/AWS-1-10/main/README.md?token=GHSAT0AAAAAACFG2HWWQ26WSDMIVSKQC7LAZJT7RYA"
fileName = "README.md"

# Baixando o arquivo da Internet
import os
os.system(f"wget {url} -O {fileName}")

# Carregando o arquivo como um RDD de linhas
textRDD = spark.sparkContext.textFile(fileName)

# Dividindo as linhas em palavras, removendo caracteres especiais e convertendo para letras minúsculas
wordsRDD = textRDD.flatMap(lambda line: line.split(" ")).map(lambda word: word.lower().replace("[^a-zA-Z0-9]", ""))

# Filtrando palavras vazias
filteredWordsRDD = wordsRDD.filter(lambda word: word != "")

# Mapeiando cada palavra para um par (palavra, 1)
wordPairsRDD = filteredWordsRDD.map(lambda word: (word, 1))

# Reduzindo as palavras contando ocorrências
wordCount = wordPairsRDD.reduceByKey(lambda a, b: a + b)

# Exibindo o resultado
wordCount.foreach(print)

# Encerrando a sessão Spark
spark.stop()

