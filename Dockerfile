FROM apache/spark:3.5.1

WORKDIR /app
COPY job.py /app/
COPY data.csv /app/

CMD ["/opt/spark/bin/spark-submit", "/app/job.py"]
