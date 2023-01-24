import pika
from pika.exchange_type import ExchangeType

def callback(ch,method,properties,body):
    print(f'First Consumer:{body}')

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

queue=channel.queue_declare(queue='')

channel.queue_bind(exchange='pubsub', queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=callback)

print('Started consuming')

channel.start_consuming()