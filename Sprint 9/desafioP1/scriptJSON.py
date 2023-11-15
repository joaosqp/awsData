import sys
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

# Leitura dos arquivos JSON
df = spark.read.json(source_path)

# Extrair a data de coleta do caminho do arquivo
data_coleta = "2023-11-07"

# Escrever os dados no formato Parquet com o nome do arquivo contendo a data
df.write.mode("append").parquet(f"{target_path}/data_coleta={data_coleta}")
