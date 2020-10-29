# Completed as part of Data Engineering W205 for Berkeley Masters of Information and Data Science, Oct 2020
Goal of project was to build an ETL with Docker. An ETL Pipeline refers to a set of processes extracting data from an input source, transforming the data, and loading into an output destination. 

I spun all components up in Docker, published and consumed a large json file with Kafka, transformed the message using JQ in Apache Spark and finally stored the results (a cleaned Json query) to HDFS (Hadoop Distributed File Storage). 

As always, collaboration welcome! 
---------------------------------------
# Prompt
Prepare the infrastructure to land the data in the form and structure it needs
to be to be queried.  You will need to:

- Publish and consume messages with Kafka
- Use Spark to transform the messages. 
- Use Spark to transform the messages so that you can land them in HDFS

You should include your `docker-compose.yml` used for spinning the pipeline. One example is enough!

You can either run Spark through the command line or use a notebook. If you use
the command line, add an annotated markdown file where you present your results,
tools used, and explanations of the commands that you use. 
To get the history from Spark run

```
docker-compose exec spark cat /root/.python_history
```

You should be able to query your data at the end. 

In order to show the data scientists at these other companies the kinds of data
that they will have access to, decide on 1 to 3 basic business questions that
you believe they might need to answer about these data.

