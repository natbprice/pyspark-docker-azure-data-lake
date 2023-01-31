FROM apache/spark-py:3.3.1
USER root
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN mkdir $SPARK_HOME/conf && \
    echo "spark.jars.packages org.apache.hadoop:hadoop:azure:3.3.1" > $SPARK_HOME/conf/spark-defaults.conf && \
    echo "spark.driver.maxResultSize = 0" >> $SPARK_HOME/conf/spark-defaults.conf