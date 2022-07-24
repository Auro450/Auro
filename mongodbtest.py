import pymongo
client = pymongo.MongoClient("mongodb+srv://Auro:Auro@cluster0.e9n49sf.mongodb.net/?retryWrites=true&w=majority")
db1 = client.get_database("school_database")
schools = db1.school_1
schools.count_documents({})
schools.insert_one({"name":"john" , "surname":"kund" , "subject":"chem" , "code":15})









