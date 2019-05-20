#import paho.mqtt.client as paho
#import paho.mqtt.client as mqtt
#broker="192.168.10.34"
#broker="192.168.10.147"
#port=1883
#client = mqtt.Client()
#def on_publish(client,userdata,result):             #create function for callback
#    print("data published \n")
#    pass
#client1 = paho.Client("control1")                           #create client object
#client1.on_publish = on_publish                          #assign function to callback
#client.connect(broker,port)                                 #establish connection
#ret= client1.publish("Topic","on")                   #publish
#client.subscribe('#')
#def on_message( client, userdata, msg):
#    print("Ajuste: ",float(msg.payload)," Celsius.")
#    print("Esperando nuevo valor tipo string2float.")
#pass
#client.on_message = on_message
#client.loop_forever()



import paho.mqtt.client as mqtt #import the client1
broker_address="192.168.10.34"
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
client.connect(broker_address) #connect to broker
client.publish("Topic","12")#publis