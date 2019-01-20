# kafka_utils

##### Some python applications to creating kafka connectors using Kafka Connect REST Interface, to create avro schemas using Schema Registry API provide by confluent, CRUD operations on kafka topics using confluent_kafka library for python provide by confluent, little samples to produce or consume message in avro format from kafka topics, CRUD operations on streams / tables in ksql provided by confluent, etc.

##### Some utilities to help developers work with kafka enviroment.

##### Under construction !!!!

##### Enjoy!

***
## Pre-reqs (commands to install on linux)

Python 3.6.5 or higher:
> `sudo apt install python3`

Python3-pip or pip3:
> `sudo apt install python3-pip`

After, you need to install all python librarys we will need:
> `sudo pip3 install -r requirements.txt`


## Download

Create a folder, and inside this folder, run the follow command to download the flinox/kafka_utils:
> `git clone https://github.com/flinox/kafka_utils.git`


## CRUD Topics
> `crud_topics.py`

Utility to manage kafka topics, is basically the sample **[confluent-kafka-python - sample](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py)** with a little change in create topic, to pass as a parameter the quantity of partitions and replicas

### Sintaxe: 
> `python crud_topics.py <brokers> <operation> <arg1> <arg2> ...`

#### Brokers: 
>* `Your kafka brokers, sample:`
>* `hostname_or_ip1:port,hostname_or_ip2:port`

#### Operations:
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



## Create Connector Thru Connect REST API
> `create_connector.py`

Utility to create a connector using Connect REST API, this program will read the .properties file and convert to json format to pass as content to API, it will try to create, if exists will update the connector. 

### Sintaxe: 
> `python create_connector.py ./connectors/kafka-tabela.properties <hostname_or_ip_connect_rest_api>:8083 --schema_registry_cloud=<hostname_or_ip_schema_registry_rest_api>:8081`

#### Hostname or ip of Connect REST API machine: 
>* `The hostname_/ ip address of the machine running the Connect REST API to create the connector`

#### Schema_Registry_Cloud: 
>* `This parameter is optional, I use it to create a connector in another Schema Registry machine, so if you use this parameter, the program will override the value.converter.schema.registry.url and key.converter.schema.registry.url when convert the .properties to .json file, the value informed will only persist in the json file`
