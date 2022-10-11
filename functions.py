import pymongo
from bson.objectid import ObjectId
from datetime import datetime
import json
now = datetime.now()
dateAndTime = now.strftime("%Y/%m/%d, %H:%M:%S")
myclient = pymongo.MongoClient("mongodb://localhost:27017/")



def convertPayloadToCorrectFormat(inData, datetime:datetime):
    sensorData = inData[2:-1]
    document = json.loads(sensorData)
    payloadlvl1 = document["uplink_message"]
    payloadlvl2 = payloadlvl1["decoded_payload"]
    idLvl1 = document["end_device_ids"]
    idLvl2 = idLvl1["device_id"]
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


# updateDocumentById("testData", "customers", "633fdc5d9e39c2cab67b7c9c", "name", "Robert")
# updateDocumentById("testData", "customers", "633fdc5d9e39c2cab67b7c9c", "address", "Sigurdsgatan 20")

#en funktion där man med hjälp av _id hittar och kör delete på ett dokument i en specifik collection
def removeDocumentById(databaseToUpdate:str, collectionToUpdate:str ,idToUpdate:str, iAmSure:bool):
    database = myclient[databaseToUpdate]
    collection = database[collectionToUpdate]
    query = {'_id': ObjectId(idToUpdate)}
    if iAmSure == True:
        collection.delete_one(query)

#removeDocumentById("testData", "customers", "633fe16101d1eec1c4dc560f", True)


#en funktion som returnerar ett dokument
def queryDocumentById(databaseToQuery:str, collectionToQuery:str ,idToQuery:str):
    database = myclient[databaseToQuery]
    collection = database[collectionToQuery]
    query = {'_id': ObjectId(idToQuery)}
    documentSearchedFor = collection.find(query)
    return documentSearchedFor

# search = queryDocumentById("testData", "customers", "633fdc5d9e39c2cab67b7c9c")
# for x in search:
#   print(x)
