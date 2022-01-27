
import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kd1i6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url)
db =client["pytech"]
collection = db["students"]

post1 = {
            "student_id": 1007, 
            "first_name": "Marry", 
            "last_name": "Python",
            "enrollment": [
                {
                    "term": "winter",
                    "gpa": "3.5",
                    "start_date": "November 26, 2021",
                    "end_date": "March 07, 2022"
                },
            ],
                "course": [
                {
                    "course_id": 1007,
                    "description": "Network Security",
                    "instructor": "Jones",
                    "grade": "A"
                }
            ]
       }

post2 = {
            "student_id": 1008, 
            "first_name": "Jerry", 
            "last_name": "Python",
            "enrollment": [
                {
                    "term": "winter",
                    "gpa": "2.5",
                    "start_date": "November 26, 2021",
                    "end_date": "March 07, 2022"
                },
            ],
                "course": [
                {
                    "course_id": 1008,
                    "description": "IT Security",
                    "instructor": "James",
                    "grade": "B"
                }
            ]
       }

post3 = {
            "student_id": 1009, 
            "first_name": "Paul", 
            "last_name": "Purple",
            "enrollment": [
                {
                    "term": "winter",
                    "gpa": "3.0",
                    "start_date": "November 26, 2021",
                    "end_date": "March 07, 2022"
                },
            ],
                "course": [
                {
                    "course_id": 1009,
                    "description": "Database Security",
                    "instructor": "Jones",
                    "grade": "A"
                }
            ]
       }      


print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
result = collection.find({
    "student_id": {"$gte":1007}})

for doc in result.sort('student_id', pymongo.ASCENDING):
    print(" Student ID:", doc["student_id"], "\n","First Name:", doc["first_name"], "\n", "Last Name:", doc["last_name"],"\n")


print(" -- INSERT STATEMENTS --")
post4 = {
    "student_id": 1010,
    "first_name": "John",
    "last_name": "Doe"
}
result = collection.insert_one(post4)

print("Inserted student record into the students collection with documented_id", result.inserted_id,"\n")

print(" -- DISPLAYING STUDENT TEST DOC --")
result = collection.find_one({"student_id": {"$eq": 1010}})
print(" Student Name:", result["student_id"], "\n", "First Name:", result["first_name"], "\n", "Last Name:", result["last_name"], "\n")   

result = collection.delete_one({"student_id": 1010})

print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
result = collection.find({
    "student_id": {"$gte":1007}})

for doc in result.sort('student_id', pymongo.ASCENDING):
    print(" Student ID:", doc["student_id"], "\n","First Name:", doc["first_name"], "\n", "Last Name:", doc["last_name"],"\n")
