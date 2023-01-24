import pika
import time
import random

connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='q1')
messageID=1
while(True):
    message=f'Message: {messageID}'
    channel.basic_publish(exchange='',routing_key='q1',body=message)
    print(f'Message: {messageID} sent')
    time.sleep(random.randint(1,4))
    messageID+=1