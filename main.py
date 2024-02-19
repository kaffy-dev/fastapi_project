# Create a student resource with id(int), name(str), age(int), sex(str), height(float)
# Use an in-memory dictionary to store data
# Create end points to do the following
# Create a student resource (Post)
# Retrieve a student resource for one and many students (Get)
# Update a student resource (Put)
# Delete a student resource (Delete)
# Use basic python
from fastapi import FastAPI
from uuid import UUID 
from typing import Optional

app = FastAPI()

students = {}

student_data = {
    "id": 0,
    "name": "",
    "age": 0,
    "sex": "",
    "height": 0
}

@app.get('/')
def home():
    return {"message: This is a student API"}

# Get all books
@app.get('/students')
def get_all_students():
    return {"message": "Successfully retrieved", "data": students}

# Get a single student by id
@app.get('/students/{id}')
def get_single_student(id):
    student = students.get(id)
    if not student:
        return "Student not found"
    return {"message": "success", "data": student}

# Add/Create a new student
@app.post('/students')
def add_student(name: str, age, sex: str, height: float):
    new_student = student_data.copy()

    id_ = len(students) + 1
    uuid_id = str((UUID(int=id_)))
    new_student['id'] = uuid_id
    new_student['name'] = name
    new_student['age'] = age
    new_student['sex'] = sex
    new_student['height'] = height

    students[new_student["id"]] = new_student
    return {"message": "Successfully created a new student", "data": new_student}

# Update student
@app.put('/students/{id}')
def update_student(id: str, name: Optional[str] = None, age: Optional[int] = None, sex: Optional[str] = None, height: Optional[float] = None):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}
    if name is not None:
        student['name'] = name
    if age is not None:
        student['age'] = age
    if sex is not None:
        student['sex'] = sex
    if height is not None:
        student['height'] = height
    return {"message": "Student updated successfully", "data": student}


# Delete student
@app.delete('/students/{id}')
def delete_student(id):
    student = students.get(id)
    if not student:
        return {"error": "Student not found"}
    del students[id]
    return {"message": "Student deleted successfully"}