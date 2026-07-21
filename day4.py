first_name = "Elijah"
last_name = "Wambui"
age = 20
height = "5'8\""
weight = 52
university = "Jomo Kenyatta University of Agriculture and Technology"
course = "Information Technology"

def myfunc():
    global course
    course = "Data Science"
    
myfunc()
print("FIRST_NAME : ", first_name)
print("LAST_NAME : ", last_name)
print("AGE : ", age)
print("HEIGHT : ", height)
print("WEIGHT : ", weight)
print("UNIVERSITY : ", university)
print("COURSE : ", course)
