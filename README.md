# Kafka_utils

##### Some python applications to creating kafka connectors using Kafka Connect REST Interface, to create avro schemas using Schema Registry API provide by confluent, CRUD operations on kafka topics using confluent_kafka library for python provide by confluent, little samples to produce or consume message in avro format from kafka topics, CRUD operations on streams / tables in ksql provided by confluent, etc.

##### Some utilities to help developers work with kafka enviroment.

##### Enjoy!

***

## CRUD Topics
> `crud_topics.py`

Utility to manage kafka topics, is basically the sample **[confluent-kafka-python - sample](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py)** with a little change in create topic, to pass as a parameter the quantity of partitions and replicas

### Sintaxe: 
> `python crud_topics.py <brokers> <operation> <arg1> <arg2>`

### Operations:
>* `create_topic`
>* `create_partitions`
>* `describe_configs`
>* `alter_configs`
>* `delta_alter_configs`
>* `delete_topics`
>* `list`

### Samples:

#### Create topic
>##### `python crud_topics.py <brokers> create_topic <topic_name> <qty_partitions> <qty_replicas>`
>![Topic created](/images/crud_topics_create.jpg)
>![When you list the topic created to check](/images/crud_topics_create_list.jpg)

#### Create partitions
>##### `python crud_topics.py <brokers> create_partitions <topic_name> <new_total_partitions>`
>![Topic created](/images/crud_topics_partition_create.jpg)
>![When you list the topic created to check](/images/crud_topics_partition_create_list.jpg)

#### Describe configs
>##### `python crud_topics.py <brokers> describe_configs <topic_name> <new_total_partitions>`
>![Topic created](/images/crud_topics_partition_create.jpg)
>![When you list the topic created to check](/images/crud_topics_partition_create_list.jpg)

#### Delete topics
>##### `python crud_topics.py <brokers> delete_topics <topic_name1> <topic_name2> ...`
>![Topic deleted](/images/crud_topics_delete.jpg)

#### List topics
>##### `python crud_topics.py <brokers> list topics`
>![List topics](/images/crud_topics_list.jpg)

#### List brokers
>##### `python crud_topics.py <brokers> list brokers`
>![List brokers](/images/crud_topics_brokers.jpg)

#### List all
>##### `python crud_topics.py <brokers> list all`
>![List topics and brokers](/images/crud_topics_all.jpg)





describe_configs <resource_type1> <resource_name1> <resource2> <resource_name2> ..
alter_configs <resource_type1> <resource_name1> <config=val,config2=val2> <resource_type2> <resource_name2> <config..>
delta_alter_configs <resource_type1> <resource_name1> <config=val,config2=val2> <resource_type2> <resource_name2> <config..> ..

