#1

def register_student(name, age, course="Computer Science"):
    student_info = {
        "name": name,
        "age": age,
        "course": course
    }
    return student_info


print(register_student("Eli", 20))

#2

def calculate_salary(name, hours_worked, hourly_rate, tax_rate=0.10):
    gross_salary = hours_worked * hourly_rate
    tax_amount = gross_salary * tax_rate
    net_salary = gross_salary - tax_amount
    
    print(f"Employee: {name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Hourly Rate: {hourly_rate}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Tax: {tax_amount}")
    print(f"Net Salary: {net_salary}")


calculate_salary("Kelvin", 40, 500)

#3

def book_flight(passenger_name, destination, seat_class):
    print(f"Passenger: {passenger_name}, Destination: {destination}, Seat Class: {seat_class}")

# Positional arguments
book_flight("Alice", "Nairobi", "Business")

# Keyword arguments
book_flight(destination="Mombasa", seat_class="Economy", passenger_name="Brian")

#4

school = "Coding Time"  # Global variable

def display_school():
    print(school)

display_school()

def show_teacher():
    teacher = "Mr. James"  # Local variable
    print(teacher)

show_teacher()

#5

import json

student = register_student("Eli", 20)
student_json = json.dumps(student)
print(student_json)
