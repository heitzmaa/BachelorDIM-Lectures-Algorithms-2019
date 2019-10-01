# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:58:54 2019

@author: heitzmaa
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Test d'un flux d'information PC->CloudAMQP->PC
Test step 1: avec le mode 'SEND' ligne 14, lancer plusieurs fois le script pour lancer plusieurs messages dans la file dédiée dans cloudamqp
Test step 2: modifier la ligne 14 en mettant autre chose que 'SEND' dans la variable mode et lancer le script. Celui ci doit alors dépiler les messages envoyés dans le cloud et les afficher
"""
#import urlparse
import os
import pika


mode='_SEND' #set 'SEND' mode is you will to send rather than receive messages


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)



amqp_url='amqp://hgbfmijp:6ifc4pb8q3E1ekXbEv2QJxA-j9fLonea@hedgehog.rmq.cloudamqp.com/hgbfmijp'


# Parse CLODUAMQP_URL (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params) # Connect to CloudAMQP

channel = connection.channel()

channel.queue_declare(queue='presentation')


if mode == 'SEND':
    channel.basic_publish(exchange='',
                          routing_key='presentation',
                          body='Antoine Heitzmann')
                          
    print(" [x] Sent 'Antoine Heitzmann!'")
    
    connection.close()
else:
        
   # newer pika version
    channel.basic_consume(queue='presentation',
                          on_message_callback=callback,                          
                          auto_ack=True)
   
   #older pika version
   # channel.basic_consume(callback,queue='presentation',no_ack= False)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

