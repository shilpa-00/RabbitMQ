import pika

def callback(ch,method,properties,body):
    print(f'{body} consumed')

connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()
channel.queue_declare(queue='simplequeue')
channel.basic_consume(queue='simplequeue', on_message_callback=callback,auto_ack=True)
print('Started consuming')
channel.start_consuming()