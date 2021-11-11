from pymongo import MongoClient
from bson.json_util import dumps
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uri = "mongodb://localhost:27017/test"
    client = MongoClient(uri)
    campusDB = client.campusManagementDB
    students = campusDB.students
    cursor = students.find({"lastName":"Parker"})
    print(dumps(cursor,indent=4))
    student = students.insert_one({"firstName":"John","lastName":"Doe","email":"john.doe@gmail.com","studentId":2021222})

    students_list = [
        {"firstName":"Savitri","lastName":"Patel","email":"savitri.patel@gmail.com"},
        {"firstName":"Parvati","lastName":"Patel","email":"Parvati.patel@gmail.com"}]

    students.insert_many(students_list)

    # student = students.find_one({"lastName":"Doe"})
    # student["onlineOnly"] = True
    # student["email"] = "johnd@campus.edu"
    # students.replace_one({"lastName":"Doe"},student)
    #print(dumps(students.find({"lastName":"Doe"}),indent = 4))
    #print(dumps(students.count_documents()))


