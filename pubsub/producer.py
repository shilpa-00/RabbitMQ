#RabbitMQ using docker image
#docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management

import pika
from pika.exchange_type import ExchangeType

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

message='hello'

channel.basic_publish(exchange='pubsub',routing_key='',body=message)

print('Msg sent')

connection.close()