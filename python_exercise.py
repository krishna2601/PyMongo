from pymongo import MongoClient

#connection string
connectionUrl = "mongodb://localhost:27017/test"

#connect to the database
connection = MongoClient(connectionUrl)

#select the database training
db = connection.training

#select the collection mongodb_glossary
collection = db['mongodb_glossary']

#insert the document in a collection
data = [{"database":"a database contains collections"},
        {"collection":"a collection stores the documents"},
        {"document":"a document contains the data in the form or key value pairs."}]

#insert multiple rows in a databse
db.collection.insert_many(data)


#display all the collection in a mongodb
docs = db.collection.find()

#print all the document in a document
for doc in docs:
    print(doc)




connection.close()