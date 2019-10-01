# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:33:27 2019

@author: heitzmaa
"""
import os
import pika
import argparse

amqp_url='amqp://hgbfmijp:6ifc4pb8q3E1ekXbEv2QJxA-j9fLonea@hedgehog.rmq.cloudamqp.com/hgbfmijp'  
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
 # Connect to CloudAMQP
    

parser = argparse.ArgumentParser()
parser.add_argument("--read", help="activate the read mode", action="store_true")
args = parser.parse_args()


cpt=0

if args.read==True:
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    cpt=0
    
    def callback(ch, method, properties, body):
        global cpt
        cpt += 1
        print(" [x] Received %r" % body)
        print("number of msg :" ,cpt)
      
        
    channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                          
                              auto_ack=True)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    channel.start_consuming()

else :
   connection = pika.BlockingConnection(params) # Connect to CloudAMQP
   channel = connection.channel()
   channel.queue_declare(queue='presentation')
   channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Antoine Heitzmann')
                          
   print(" [x] Sent 'Antoine Heitzmann!'")
   connection.close()