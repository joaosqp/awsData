import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, count, upper

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

from pyspark.sql.functions import *

df = spark.read.format("csv").option("header", "true").load(source_file)

df = df.withColumn("nome", upper(col("nome"))).sort(col("ano").desc())

df.count()

df.createOrReplaceTempView("nomes")

spark.sql("""
    SELECT nome, ano
    FROM nomes
    WHERE sexo = 'F'
    ORDER BY total DESC
    LIMIT 1
""").show()

spark.sql("""
    SELECT nome, ano
    FROM nomes
    WHERE sexo = 'M'
    ORDER BY total DESC
    LIMIT 1
""").show()

spark.sql("""
    SELECT ano, sexo, SUM(total) as total_registros
    FROM nomes
    GROUP BY ano, sexo
    ORDER BY ano
    LIMIT 10
""").show()
job.commit()

df.write.partitionBy("sexo", "ano").json(target_path)