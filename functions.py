import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb://localhost:27017/")



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
