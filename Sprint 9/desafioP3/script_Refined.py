import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME, S3_INPUT_PATH_0, S3_INPUT_PATH_1, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_0', 'S3_INPUT_PATH_1', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path_0 = args['S3_INPUT_PATH_0']
source_path_1 = args['S3_INPUT_PATH_1']
target_path = args['S3_TARGET_PATH']

df1 = spark.read.parquet(source_path_0)
df2 = spark.read.parquet(source_path_1)

df1.createOrReplaceTempView("df1")
df2.createOrReplaceTempView("df2")

df_filmes = spark.sql("""
SELECT DISTINCT
    df1.id,
    df1.titulopincipal,
    df1.anolancamento,
    df1.tempominutos,
    df1.notamedia,
    df1.numerovotos,
    df2.receita,
    df2.orcamento
FROM df1
INNER JOIN df2
    ON df1.id = df2.id
""")

df_artista = spark.sql("""
SELECT DISTINCT
    df1.generoartista,
    df1.nomeartista,
    df2.id
FROM df1
INNER JOIN df2
    ON df1.id = df2.id
""")

destino1 = 'Tabela_1'
destino2 = 'Tabela_2'

df_filmes.write.mode("append").parquet(f'{target_path}/{destino1}')
df_artista.write.mode("append").parquet(f'{target_path}/{destino2}')

job.commit()
