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
                    "course_id": "1008",
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
        


doc = db.
print(student_id)