import pika

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='simplequeue')
channel.basic_publish(exchange='',routing_key='simplequeue',body='Hello')
print('Msg sent')
connection.close()