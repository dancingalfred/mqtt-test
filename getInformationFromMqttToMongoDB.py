import paho.mqtt.client as mqtt #import the client
import time
#from functions import 

sensorDataList =[]

def on_message(client, userdata, message):
    print(message.topic+" "+str(message.payload))
    print("message received " ,str(message.payload.decode("utf-8")))
    x = (message.topic+" "+str(message.payload))
    sensorDataList.append(x)


def addToDatabaseAndThenRemoveFromList(list:list):
        if len(list) >= 1:
            print("------sensorData-----------", list[0])
            list.remove(list[0])

    
#  NNSXS.JLAUBPS72BGVVQ4EY2Y6NRWPXAXC6YTBWOWELGA.2WD3PPT7IC4X63WXUVETFIV2GDLVJ4HT4LH25TXXFAKLD5QUADXQ
#  eu1.cloud.thethings.network:1883
while True:   
    broker_address="broker.mqttdashboard.com" 
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
    addToDatabaseAndThenRemoveFromList(sensorDataList)

    time.sleep(8) # wait
    #client.loop_stop() #stop the loop



