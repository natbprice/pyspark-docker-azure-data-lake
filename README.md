# Docker PySpark with ADLS Gen2 (Azure Data Lake Storage)
This Docker image can be used to run PySpark analyses with data stored in ADLS Gen2 Storage (Azure Data Lake Storage). This image can be run locally for development/testing or deployed to a large VM as a *fast*, *simple*, and *low-cost* method of running PySpark analyses on a single node.

See:
- [Benchmarking Apache Spark on a Single Node Machine](https://www.databricks.com/blog/2018/05/03/benchmarking-apache-spark-on-a-single-node-machine.html)
- [Run Spark Jobs on Azure Batch using Azure Container Registry and Blob storage](https://medium.com/datamindedbe/run-spark-jobs-on-azure-batch-using-azure-container-registry-and-blob-storage-10a60bd78f90)

## Build Image

Before building the image, Python package dependencies are specified in the `requirements.in` file and compiled using [pip-tools](https://github.com/jazzband/pip-tools) to generate pinned package versions in `requirements.txt`:

```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pip-tools
pip-compile requirements.in
```

Build the image:

```
docker build -t spark_adls .
```

## Run PySpark Shell
Start the [PySpark shell](https://spark.apache.org/docs/latest/quick-start.html#interactive-analysis-with-the-spark-shell) for interactive use:

```
docker run -it --rm \
    -p 4040:4040 \
    spark_adls \
    /opt/spark/bin/pyspark
```

## Run Python Script
Run a Python script by attaching current directory as a volume and calling [spark-submit](https://spark.apache.org/docs/latest/submitting-applications.html):

```
docker run -it --rm \
    -v $(pwd):/opt/spark/work-dir \
    -p 4040:4040 \
    spark_adls \
    /opt/spark/bin/spark-submit --driver-memory 2g /opt/spark/work-dir/test.py
```