# kafka_utils

##### Some python applications to creating kafka connectors using Kafka Connect REST Interface, to create avro schemas using Schema Registry API provide by confluent, CRUD operations on kafka topics using confluent_kafka library for python provide by confluent, little samples to produce or consume message in avro format from kafka topics, CRUD operations on streams / tables in ksql provided by confluent, etc.

##### Some utilities to help developers work with kafka enviroment.

##### Under construction !!!!

##### Enjoy!

***
## Pre-reqs

Python 3.6.5 or higher:
> `sudo apt install python3`

Python3-pip or pip3:
> `sudo apt install python3-pip`

Python librarys:
> `sudo pip3 install -r requirements.txt`


## Download

Now download this package on your folder:
> `git clone https://github.com/flinox/kafka_utils.git`

***
## CRUD Topics
> `crud_topics.py`

Utility to manage kafka topics, is basically the sample **[confluent-kafka-python - sample](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py)** with a little change in create topic, to pass as a parameter the quantity of partitions and replicas

### Sintaxe: 
> `python crud_topics.py <brokers> <operation> <arg1> <arg2> ...`

#### brokers: 
>* `Your kafka brokers, sample:`
>* `hostname_or_ip1:port,hostname_or_ip2:port`

#### operation:
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
>##### `python crud_topics.py <brokers> describe_configs topic <topic_name> `
>![Topic created](/images/crud_topics_describe_configs.png)

#### Alter configs
>##### `python crud_topics.py <brokers> alter_configs topic <topic_name> <config=val,config2=val2> `
>![Topic created](/images/crud_topics_alter_configs.png)
>![When you describe topic again](/images/crud_topics_alter_configs_describe.png)

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





## Create Connector
> `create_connector.py`

Utility to create a connector using Connect REST API, this program will read the .properties file and convert to json format to pass as content to API, it will try to create, if exists will update the connector. 

### Sintaxe: 
> `python create_connector.py ./connectors/<connector.properties> <hostname_or_ip_connect_rest_api>:8083 --schema_registry_cloud=<hostname_or_ip_schema_registry_rest_api>:8081`

#### connector.properties: 
> `The java properties file previously configured to database drivers, tables, querys, passwords, etc.`

#### hostname_or_ip_connect_rest_api: 
> `The hostname_/ ip address of the machine running the Connect REST API to create the connector`

#### schema_registry_cloud: 
> `This parameter is optional, I use it to create a connector in another Schema Registry machine, so if you use this parameter, the program will override the value.converter.schema.registry.url and key.converter.schema.registry.url when convert the .properties to .json file, the value informed will only persist in the json file`






## Consume Topic in Avro format
> `consumer_avro_topic.py`

Utility to consume topic in Avro format, it includes an override on AvroConsumer of confluent to deserialize only the values field, ignoring the key field. 

### Sintaxe: 
> `python consumer_avro_topic.py <bootstrap> <groupid> <schema_registry> <topic>`

#### bootstrap: 
> `The list of brokers kafka, ex.: localhost:9092.`

#### groupid: 
> `To control what messages was read by this groupid, simple a word to used by kafka to control what messages was readed by this groupid.`

#### schema_registry: 
> `This address to schema registry to obtain the correct schema version to deserialize the message.`

#### topic: 
> `The topic to obtain the messages.`


### Sample:

>##### `python consumer_avro_topic.py localhost:9092 sistema1 localhost:8081 alunos`
>![Topic created](/images/consumer_avro_topic.jpg)
