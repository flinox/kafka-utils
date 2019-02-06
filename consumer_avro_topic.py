## Programa exemplo para consumir mensagens de um topico em formato avro apenas para o valor
## Sintaxe de uso: python create_connector.py <caminho/nome_arquivo.properties> <hostname:8083>
## Le o arquivo .properties, converte em .json e chama API REST para criar o connector no connect
## By: Fernando Lino em 05/12/2018
## python consumer_avro_topic.py localhost:9092 groupid2 localhost:8081 test-avro

from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka.avro import AvroConsumer
import sys
import argparse

class KeyAvroConsumer(AvroConsumer):

    def __init__(self, config):
        super(KeyAvroConsumer, self).__init__(config)

    def poll(self, timeout=None):
        """
        This is an overriden method from AvroConsumer class. This handles message
        deserialization using avro schema for the value only.

        @:param timeout
        @:return message object with deserialized key and value as dict objects
        """
        if timeout is None:
            timeout = -1
        message = super(AvroConsumer, self).poll(timeout)
        if message is None:
            return None
        if not message.value() and not message.key():
            return message
        if not message.error():
            if message.value() is not None:
                decoded_value = self._serializer.decode_message(message.value())
                message.set_value(decoded_value)
            # Don't try to decode the key
        return message

def processMessage(msg):
    print(msg.value())

if __name__ == '__main__':

    # Define os parametros esperados e obrigatorios
    parser = argparse.ArgumentParser()
    parser.add_argument("bootstrap", help="Lista dos brokers kafka, ex.: localhost:9092")
    parser.add_argument("groupid", help="Informe o groupid para controlar que o consumer retorne apenas as mensagens pendentes")
    parser.add_argument("schema_registry", help="Informe o endereço para o schema registry, ex.: localhost:8081 ")
    parser.add_argument("topic", help="Informe o topico que deseja consumir")
    args = parser.parse_args()


    c = KeyAvroConsumer({
        'bootstrap.servers': args.bootstrap,
        'group.id': args.groupid,
        'schema.registry.url': 'http://'+args.schema_registry,
        'auto.offset.reset': 'earliest'})

    c.subscribe([args.topic])

    while True:
        try:
            msg = c.poll(10)

        except SerializerError as e:
            print("Message deserialization failed for {}: {}".format(msg, e))
            break

        except KeyboardInterrupt:
            sys.stderr.write('Aborted by user\n')
            break

        if msg is None:
            continue

        if msg.error():
            print("Message: {}".format(msg.error()))
            continue

        processMessage(msg)

    c.close()



