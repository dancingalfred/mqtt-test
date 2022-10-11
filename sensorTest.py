import paho.mqtt.client as mqtt #import the client
import time
#from functions import 

def on_message(client, userdata, message):
    print(message.topic+" "+str(message.payload))
    print("message received " ,str(message.payload.decode("utf-8")))


def returnPayload(client, userdata, message):
    print(message.topic+" "+str(message.payload)) #("utf-8")
    x = str(message.topic+" "+str(message.payload))
    return x
    
#  NNSXS.JLAUBPS72BGVVQ4EY2Y6NRWPXAXC6YTBWOWELGA.2WD3PPT7IC4X63WXUVETFIV2GDLVJ4HT4LH25TXXFAKLD5QUADXQ
#  eu1.cloud.thethings.network:1883
while True:   
    broker_address="eu1.cloud.thethings.network:1883" 
    print("creating new instance") 
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback
    #print(f"Detta är vad y innehåller: {y}")
    print("connecting to broker")
    client.connect(broker_address)#connect to broker
    client.loop_start() #start the loop
    print("Subscribing to topic","testtopic/4")
    client.subscribe("testtopic/4")
    print("Publishing message to topic","testtopic/4")
    client.publish("testtopic/4","OFF")
    jjj = client.on_message
    print("-----------------", jjj)

    time.sleep(5) # wait
    #client.loop_stop() #stop the loop


#'decoded_payload":{"humidity":36,"temperature":23.2,"vdd":3625,"waterleak":0'







