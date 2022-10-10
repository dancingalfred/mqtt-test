import paho.mqtt.client as mqttclient 
import time

connected = False
messagerecieved = False

def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("client is connected")
        global connected
        connected = True
    else:
        print("client is not connected")    



def on_messag(client,userdata,message):
    print("Message recived"+ str(message.payload.decode("utf-8")))
    print("Topic"+str(message.topic))
 

broker_address="eu1.cloud.thethings.network"
port = 1883
user ="ap-addiva-01@ttn"
password = "NNSXS.CMXLHF5PDRWJRHZKSWRIWXBKHXG5JGPCRCBDRWQ.LTKEJO7OU6IHPJR7V4WSRGU5IQFHW24MUQ7H77SPOOT66KUMUKLA"

clinet = mqttclient.Client("Mqtt")
clinet.username_pw_set(user,password=password)
clinet.on_connect = on_connect
clinet.connect(broker_address,port=port)
clinet.loop_start()
clinet.subscribe("ap-addiva-01@ttn")

while connected != True:
    time.sleep(0.2)

while messagerecieved != True:
    time.sleep(0.2)

# clinet.loop_stop()
