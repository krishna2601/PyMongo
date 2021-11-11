from pymongo import MongoClient



connection_url  = "mongodb://localhost:27017/test"

#connect to mongodb server
print("Connecting to the mongodb server...")
connection = MongoClient(connection_url)

#select the 'training' database
db = connection.training

#create collection
collection = db["python"]

#create a sample document
doc = {'lab':'Accessing the mongodb using python','Subject':'No SQL Databases'}

#insert a sample document
print("Inserting a document into collection...")
db.collection.insert_one(doc)

#print all the doucments in a collection
docs = db.collection.find()

print("Printing the documents in the collection...")
for document in docs:
    print(document)

print("Closing the connection.")
connection.close()

