dictionary = {
        "name": "John",
        "age": 21
}

print(dictionary["name"])  # Output: John

#.get()

student = {
    "name": "Alice",
    "School": "UoN",
    "course": "Agriculture"
}

print(student)

#Adding new items.
student["Email"] = "Alice29012@gmail.com"
student["Phone"] = "0712345678"

print(student)

student.pop("course")  

print(student)

del student["School"]

print(student)

print("Keys: ")
for key in student.keys():
    print(key)

print("\nValues: ")
for value in student.values():
    print(value)

print("\nKeys and Values: ")
for key, value in student.items():
    print(f"{key}: {value}")


#Nested Dictionary
Students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    },
    "student3": {
        "name": "Charlie",
        "age": 21
    }
}

#Accessing the information
print("student1 Name: ",
Students["student1"]["name"])