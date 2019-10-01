
import os
import pika



amqp_url='amqp://hgbfmijp:6ifc4pb8q3E1ekXbEv2QJxA-j9fLonea@hedgehog.rmq.cloudamqp.com/hgbfmijp'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='presentation')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    
channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()