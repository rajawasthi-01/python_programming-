students = [
    {
        "name": "Raj",
        "usn": "1MS21CS001",
        "age": 19,
        "semester": 5,
        "marks": 88
    },
    {
        "name": "Bob",
        "usn": "1MS21CS002",
        "age": 20,
        "semester": 5,
        "marks": 92
    },
    {
        "name": "Charlie",
        "usn": "1MS21CS003",
        "age": 18,
        "semester": 5,
        "marks": 85
    }
]

for student in students:
    print(f"Name: {student['name']}, USN: {student['usn']}, Age: {student['age']}, Semester: {student['semester']}, Marks: {student['marks']}")
