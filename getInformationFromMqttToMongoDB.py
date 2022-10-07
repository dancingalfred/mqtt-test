import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def returnPayload(client, userdata, message):
     x = str(message.payload.decode("utf-8"))
     return x
while True:   
    ########################################
    broker_address="broker.mqttdashboard.com" 
    #broker_address="iot.eclipse.org"
    print("creating new instance")
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    y = client.on_message=on_message
    print(f"Detta är vad y innehåller: {y}")
    print("connecting to broker")
    client.connect(broker_address)#connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","testtopic/4")
    client.subscribe("testtopic/4")
    print("Publishing message to topic","testtopic/4")
    client.publish("testtopic/4","OFF")
    time.sleep(2) # wait
    #client.loop_stop() #stop the loop
    

