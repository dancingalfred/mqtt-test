#import context
from functions import addDocumentToDatabase
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt #import the client
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["testData"]
mycol = mydb["sensordata"]

m = subscribe.simple(topics=['#'], hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"ap-addiva-01@ttn",'password':"NNSXS.GB7LQUCAHNXYDZ65KIS4FV2JDQYVJMYK42DBT2Q.CJ3VVVVKOPIYACEXK45WK6XPTL2QIGC6DIL6JZ2YK3OHLMAEEC7Q"}, msg_count=2)
for a in m:
    print("---------------------------TOPIC-START----------------------------")
    print(a.topic)
    print("---------------------------TOPIC-END----------------------------")
    print("---------------------------PAYLOAD-START----------------------------")
    print(a.payload)
    document = str(a.payload)
    document = document[700:775]
    
    addDocumentToDatabase("testData", "sensordata", document)
    print("---------------------------PAYLOAD-START----------------------------")