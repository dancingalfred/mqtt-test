import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

def convertPayloadToCorrectFormats(inData) -> dict:
    data_from_sensor =inData.payload.decode("utf-8")
    data_to_dict =  json.loads(data_from_sensor)
    div_id = data_to_dict["end_device_ids"]["device_id"]
    result = data_to_dict["uplink_message"]["decoded_payload"]
    print(div_id)
    print(result)


def convertPayloadToCorrectFormat(inData) -> dict:
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

    if idLvl2 == "eui-a81758fffe075b66":
        fixed_document = {"Sensor address": "Skrivbord Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe075b65":
        fixed_document = {"Sensor address": "Pingisrum Addiva Sigurdsgatan"}
        fixed_document.update(document)
    elif idLvl2 == "eui-a81758fffe075c91":
        fixed_document = {"Sensor address": "Matsal Addiva Sigurdsgatan"}
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

#en funktion som returnerar ett dokument
def queryDocumentById(databaseToQuery:str, collectionToQuery:str ,idToQuery:str):
    database = myclient[databaseToQuery]
    collection = database[collectionToQuery]
    query = {'_id': ObjectId(idToQuery)}
    documentSearchedFor = collection.find(query)
    return documentSearchedFor