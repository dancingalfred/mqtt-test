import paho.mqtt.subscribe as subscribe
from functions import addDocumentToDatabase, convertPayloadToCorrectFormat, queryTrafikverketAPI, predictTemp
import time
from datetime import datetime
from datetime import timedelta

#get current weather from api.trafikinfo.trafikverket.se
infoFromTF = queryTrafikverketAPI()
#set current time
currentTime = datetime.now()
while True:
    #subscribe and get results from the latest sensor readings from our app @ thetings network
    incommingSignals = subscribe.simple(topics=['#'], hostname="eu1.cloud.thethings.network", port=1883, auth={'username':"ap-addiva-01@ttn",'password':"NNSXS.GB7LQUCAHNXYDZ65KIS4FV2JDQYVJMYK42DBT2Q.CJ3VVVVKOPIYACEXK45WK6XPTL2QIGC6DIL6JZ2YK3OHLMAEEC7Q"}, msg_count=2)

    #add the readings to MongoDB with the api call and convert the payload to the format we choose
    for signal in incommingSignals:
        fixed_dictionary = convertPayloadToCorrectFormat(str(signal.payload),infoFromTF)
        addDocumentToDatabase("20221114", "sensordata", fixed_dictionary)
        print(f"added {fixed_dictionary} to sensordata")
    time.sleep(0.1)
    #every 5 minutes we get a new reading from api.trafikinfo.trafikverket.se and we also call api.tomorrow.io for the latest weatherforecast
    #for our latitude and longitude
    if datetime.now() >= currentTime + timedelta(minutes=5):
        infoFromTF = queryTrafikverketAPI()
        currentTime = datetime.now()

        predictedInsideTemp = predictTemp()

        #we print a warning if the temperature is outside our intervalls
        if predictedInsideTemp <=20.0:
            print("******Increase heat******")
            print("******Increase heat******")
            print("******Increase heat******")
            print("******Increase heat******")
        if predictedInsideTemp >=23.5:
            print("******Start cooling******")
            print("******Start cooling******")
            print("******Start cooling******")
        else:
            print("-------------------------------------")
            print("------------Values are ok------------")
            print("-------------------------------------")





