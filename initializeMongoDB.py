import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["testData"]
mycol = mydb["sensordata"]

mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)


mylist = [
  { "_id": 1,  "address": "Highway 37","tempratur":"22","Luftfuktighet":60,"VHC":"bra","PIR":"True","CO2":"1","KWH":"134","Vattenförbrukning":"2", "Datetime":"20221007:13:52:12:15646541"},
  { "_id": 2,  "address": "Lowstreet 27","tempratur":"11","Luftfuktighet":60,"VHC":"bra","PIR":"True","CO2":"1","KWH":"134","Vattenförbrukning":"10", "Datetime":"20221007:13:52:12:15646541"},
  { "_id": 3,  "address": "Apple st 652","tempratur":"14","Luftfuktighet":60,"VHC":"bra","PIR":"False","CO2":"1","KWH":"155","Vattenförbrukning":"5"},
  { "_id": 4,  "address": "Mountain 21","tempratur":"11","Luftfuktighet":30,"VHC":"bra","PIR":"True","CO2":"1","KWH":"124","Vattenförbrukning":"5"},
  { "_id": 5,  "address": "Valley 345","tempratur":"25","Luftfuktighet":30,"VHC":"bra","PIR":"False","CO2":"1","KWH":"156","Vattenförbrukning":"22"},
  { "_id": 6,  "address": "Ocean blvd 2","tempratur":"20","Luftfuktighet":30,"VHC":"bra","PIR":"False","CO2":"1","KWH":"132","Vattenförbrukning":"7"},
  { "_id": 7,  "address": "Green Grass 1","tempratur":"23","Luftfuktighet":10,"VHC":"bra","PIR":"True","CO2":"1","KWH":"122","Vattenförbrukning":"44"},
  { "_id": 8,  "address": "Sky st 331","tempratur":"11","Luftfuktighet":10,"VHC":"bra","PIR":"False","CO2":"1","KWH":"112","Vattenförbrukning":"3"},
  { "_id": 9,  "address": "One way 98","tempratur":"13","Luftfuktighet":20,"VHC":"bra","PIR":"True","CO2":"1","KWH":"121","Vattenförbrukning":"6"},
  { "_id": 10, "address": "Yellow Garden 2","tempratur":"17","Luftfuktighet":20,"VHC":"bra","PIR":"False","CO2":"1","KWH":"433","Vattenförbrukning":"55"},
  { "_id": 11, "address": "Park Lane 38","tempratur":"18","Luftfuktighet":25,"VHC":"bra","PIR":"False","CO2":"1","KWH":"344","Vattenförbrukning":"7"},
  { "_id": 12, "address": "Central st 954","tempratur":"19","Luftfuktighet":25,"VHC":"bra","PIR":"True","CO2":"1","KWH":"132","Vattenförbrukning":"22"},
  { "_id": 13, "address": "Main Road 989","tempratur":"20","Luftfuktighet":15,"VHC":"bra","PIR":"True","CO2":"1","KWH":"111","Vattenförbrukning":"8"},
  { "_id": 14, "address": "Sideway 1633","tempratur":"21","Luftfuktighet":23,"VHC":"bra","PIR":"True","CO2":"1","KWH":"145","Vattenförbrukning":"3"},
  { "_id": 15, "address": "sensor1","Luftfuktighet":23,"PIR":"True","CO2":"1","Vattenförbrukning":"3"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)




print(myclient.list_database_names())
print(mydb.list_collection_names())