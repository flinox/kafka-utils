## Kafka_utils
### By: Fernando Lino Di Tomazzo Silva

##### Some python applications to creating kafka connectors using Kafka Connect REST Interface, to create avro schemas using Schema Registry API provide by confluent, CRUD operations on kafka topics using confluent_kafka library for python provide by confluent, little samples to produce or consume message in avro format from kafka topics, CRUD operations on streams / tables in ksql provided by confluent, etc.

##### Some utilities to help developers work with kafka enviroment.

##### Enjoy!

### CRUD Topics
#### crud_topics.py

##### Utility to manage kafka topics, is basically the sample https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py with a little change in create topic, to pass as a parameter the quantity of partitions and replicas

##### Sintaxe: python crud_topics.py <brokers> <operation> <arg1> <arg2> ...

