import pika
from pika.exchange_type import ExchangeType

def callback(ch,method,properties,body):
    print(f'Second consumer:{body}')

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel=connection.channel()

queue=channel.queue_declare(queue='')

channel.exchange_declare(exchange='pubsub',exchange_type=ExchangeType.fanout)

channel.queue_bind(exchange='pubsub',queue=queue.method.queue)

channel.basic_consume(queue=queue.method.queue,auto_ack=True,on_message_callback=callback)

print('Start consuming')

channel.start_consuming()