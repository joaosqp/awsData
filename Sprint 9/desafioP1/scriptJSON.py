import sys
import pandas as pd
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_path = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

df = spark.createDataFrame(pd.read_json(f"{source_path}lote_0.json"))

for i in range(1, 7):
    df_for = spark.createDataFrame(pd.read_json(f"{source_path}lote_{i}.json"))
    df = df.union(df_for)

df.write.mode("append").parquet(target_path)

job.commit()