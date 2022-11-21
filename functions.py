import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import json
import requests
import pandas as pd


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

def convertPayloadToCorrectFormats(inData) -> dict:
    data_from_sensor =inData.payload.decode("utf-8")
    data_to_dict =  json.loads(data_from_sensor)
    div_id = data_to_dict["end_device_ids"]["device_id"]
    result = data_to_dict["uplink_message"]["decoded_payload"]
    print(div_id)
    print(result)


def convertPayloadToCorrectFormat(inData, infoFromTF) -> dict:
    document = {}
    now = datetime.now()
    dateAndTime = now.strftime("%Y/%m/%d, %H:%M:%S")
    sensorData = inData[2:-1]
    sensorDataToDict = json.loads(sensorData)
    payloadLvl1 = sensorDataToDict["uplink_message"]
    payloadLvl2 = payloadLvl1["decoded_payload"]
    idLvl1 = sensorDataToDict["end_device_ids"]
    idLvl2 = idLvl1["device_id"]
    document["sensor_id"] = str(idLvl2)
    document.update(payloadLvl2)
    document["time"] = str(dateAndTime)
    document["outside temperature (TF)"] = infoFromTF[2]
    document["outside relativeHumidity (TF)"] = infoFromTF[3]
    if infoFromTF[4] == None:
        document["precipitation (TF)"] = 0.0
    else:
        document["precipitation (TF)"] = infoFromTF[4]
    document["precipitation type (TF)"] = infoFromTF[5]
    


    if idLvl2 == "eui-a81758fffe075b66":
        fixed_document = {"Sensor address": "Skrivbord Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe075b65":
        fixed_document = {"Sensor address": "Pingisrum Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe075c91":
        fixed_document = {"Sensor address": "Matsal Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe034f66":
        fixed_document = {"Sensor address": "ERS Sensor Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe075b67":
        fixed_document = {"Sensor address": "Madelens skrivbord Addiva Sigurdsgatan"}
        fixed_document.update(document)
    return fixed_document

#en funktion som adderar valt information till databasen
def addDocumentToDatabase(databaseToAddTo:str, collectionToAddTo:str , documentToAddToDatabase:dict):
    database = myclient[databaseToAddTo]
    collection = database[collectionToAddTo]
    collection.insert_one(documentToAddToDatabase)

#en funktion där man med hjälp av _id kan hitta ett specifikt dokument och ändra valfritt attribut i det
def updateDocumentById(databaseToUpdate:str, collectionToUpdate:str ,idToUpdate:str, valueToUpdate:str, newValue:str):
    database = myclient[databaseToUpdate]
    collection = database[collectionToUpdate]
    query = {'_id': ObjectId(idToUpdate)}
    newvalues = { "$set": { valueToUpdate: newValue } }
    collection.update_one(query, newvalues)

#en funktion där man med hjälp av _id hittar och kör delete på ett dokument i en specifik collection
def removeDocumentById(databaseToUpdate:str, collectionToUpdate:str ,idToUpdate:str, iAmSure:bool):
    database = myclient[databaseToUpdate]
    collection = database[collectionToUpdate]
    query = {'_id': ObjectId(idToUpdate)}
    if iAmSure == True:
        collection.delete_one(query)

#en funktion som returnerar värden från api.trafikinfo.trafikverket.se
def queryDocumentById(databaseToQuery:str, collectionToQuery:str ,idToQuery:str):
    database = myclient[databaseToQuery]
    collection = database[collectionToQuery]
    query = {'_id': ObjectId(idToQuery)}
    documentSearchedFor = collection.find(query)
    return documentSearchedFor
def queryTrafikverketAPI():
    data = """
        <REQUEST>
            <LOGIN authenticationkey="8c981e556ca74fa7b2128c113e4eeb8c" />
            <QUERY objecttype="WeatherStation" schemaversion="1">
                    <FILTER>
                        <EQ name="Name" value="Vallby" />
                    </FILTER>            
                    <INCLUDE>Name</INCLUDE>
                    <INCLUDE>Measurement.Air.Temp</INCLUDE>
                    <INCLUDE>Measurement.MeasureTime</INCLUDE>
                    <INCLUDE>Measurement.Air.RelativeHumidity</INCLUDE>
                    <INCLUDE>Measurement.Precipitation.AmountName</INCLUDE>
                    <INCLUDE>Measurement.Precipitation.Amount</INCLUDE>
            </QUERY>
        </REQUEST>
    """
    data = data.encode('utf8')
    response = requests.post('https://api.trafikinfo.trafikverket.se/v2/data.json', data=data, headers={'Content-Type': 'text/xml'}).json()

    results = response.get('RESPONSE')
    nestedDict = results.get("RESULT")
    nestedList = nestedDict[0].get("WeatherStation")
    measurement = nestedList[0]
    stationData = measurement.get("Measurement")
    measureTime = stationData.get("MeasureTime")
    airInformation = stationData.get("Air")
    airTemperature = airInformation.get("Temp")
    airRelativeHumidity = airInformation.get("RelativeHumidity")
    precipitation = stationData.get("Precipitation")
    donwfall = precipitation.get("Amount")
    donwfallType = precipitation.get("AmountName")
    stationName = measurement.get("Name")
    return stationName, measureTime, airTemperature, airRelativeHumidity, donwfall, donwfallType




###Nedan 3 funktioner är till för att hämta data från mongoDB och skapa en dataframe till ML-alogritmerna att arbeta med
def _connect_mongo(host, port, db):
    conn = MongoClient(host, port)
    return conn[db]
def read_mongo(db, collection,queryLimit, query={}, host="mongodb://localhost", port=27017,  username=None, password=None, no_id=False):
    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, db=db)
    # Make a query to the specific DB and Collection
    cursor = db[collection].find(query).limit(queryLimit)
    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))
    # Delete the _id
    if no_id:
        del df['_id']

    return df
def generateDfFromMongoDB(host,collection, port, db, queryLimit):
    _connect_mongo(host=host, port=port, db=db)
    df = read_mongo(db, collection,queryLimit, query={}, host=host, port=port, username=None, password=None, no_id=False)
    return df


