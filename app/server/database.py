import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.AsyncIOMotorClient(MONGO_DETAILS)

database = client.students

student_collection = database.get_collection("student_collection")

#helpers
def student_helper(student)-> dict:
    return {
        "id" :str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": ["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }

#Retrieve all students present in the database
async def retrieve_students():
    students=[]
    async for student in student_collection.find():
        student.append(student_helper(student))