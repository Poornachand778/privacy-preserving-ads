# data_pipeline/spark_jobs/processor.py
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AdMetricsProcessor") \
    .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.32.0") \
    .getOrCreate()

df = spark.read.format("bigquery") \
    .option("table", "project.dataset.ads_metrics") \
    .load()