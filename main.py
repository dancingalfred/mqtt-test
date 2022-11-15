import paho.mqtt.subscribe as subscribe
from functions import addDocumentToDatabase, convertPayloadToCorrectFormat, queryTrafikverketAPI
import time
from datetime import datetime
from datetime import timedelta

infoFromTF = queryTrafikverketAPI()
currentTime = datetime.now()
while True:
    incommingSignals = subscribe.simple(topics=['#'], hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"ap-addiva-01@ttn",'password':"NNSXS.GB7LQUCAHNXYDZ65KIS4FV2JDQYVJMYK42DBT2Q.CJ3VVVVKOPIYACEXK45WK6XPTL2QIGC6DIL6JZ2YK3OHLMAEEC7Q"}, msg_count=2)

    for signal in incommingSignals:
        fixed_dictionary = convertPayloadToCorrectFormat(str(signal.payload),infoFromTF)
        addDocumentToDatabase("20221114", "sensordata", fixed_dictionary)
        print(f"added {fixed_dictionary} to sensordata")
    time.sleep(0)
    if datetime.now() >= currentTime + timedelta(minutes=5):
        infoFromTF = queryTrafikverketAPI()
        currentTime = datetime.now()








