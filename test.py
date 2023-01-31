import tensorflow as tf
from pyspark.sql import SparkSession

spark = (SparkSession
        .builder
        .appName("Spark Test")
        .master("local[*]")
        .getOrCreate())
   
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# See https://hadoop.apache.org/docs/stable/hadoop-azure/abfs.html
if os.getenv("AZURE_CLIENT_SECRET") is not None:
    # Authenticate using service principal
    spark.conf.set("fs.azure.account.auth.type", "OAuth")
    spark.conf.set("fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
    spark.conf.set("fs.azure.account.oauth2.client.id", os.environ['AZURE_CLIENT_ID'])
    spark.conf.set("fs.azure.account.oauth2.client.secret", os.environ['AZURE_CLIENT_SECRET'])
    spark.conf.set("fs.azure.account.oauth2.client.endpoint", "https://login.microsoftonline.com/{}/oauth2/token".format(os.environ['AZURE_TENANT_ID']))
else: 
    # Authenticate using managed identity
    spark.conf.set("fs.azure.account.auth.type", "OAuth")
    spark.conf.set("fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.MsiTokenProvider")

df = spark.read.parquet("abfss://{}@{}.dfs.core.windows.net/{}".format(container, account, folder))