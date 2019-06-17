# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 06:36:27 2019

@author: Ghiordy F. Contreras
"""

import paho.mqtt.client as mqtt
broker_addrzess="192.168.10.34"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("Topic","12")#publis
#client.publish("RPi","12")#publish on RPI
#client.publish("Lolin","12")#publish on Lolin
