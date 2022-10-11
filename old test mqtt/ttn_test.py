import time
import ttn
import paho.mqtt.client as mqttclient 
import time


app_id = "ap-addiva-01"
access_key = "dynamit93.NNSXS.GB7LQUCAHNXYDZ65KIS4FV2JDQYVJMYK42DBT2Q.CJ3VVVVKOPIYACEXK45WK6XPTL2QIGC6DIL6JZ2YK3OHLMAEEC7Q"


def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = mqttclient.Client("Mqtt")
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(160)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)