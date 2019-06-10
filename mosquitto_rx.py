# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 06:36:27 2019

@author: Ghiordy F. Contreras
"""

import paho.mqtt.client as mqtt
broker="192.168.10.34"
port=1883
client = mqtt.Client()
client.connect(broker,port)
client.subscribe('#')
def on_message( client, userdata, msg):
    print("Ajuste: ",float(msg.payload)," Celsius.")
    print("Esperando nuevo valor tipo string2float.")
pass
client.on_message = on_message
client.loop_forever()