import pika
import time
import random

def callback(ch,method,properties,body):
    process_time=random.randint(1,6)
    print(f'Time to process {body} is :{process_time}')
    time.sleep(process_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print('Finished processing')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='q1')

#channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='q1', on_message_callback=callback)

print('Started consuming')
channel.start_consuming()