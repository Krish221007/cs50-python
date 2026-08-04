

students = ["Harry", "Hermione", "Ron", "Draco"]

print(students[0])
print(students[1])
print(students[2])
print(students[3])
#here if the number gets bigger then we have 
# to write too many print commands so well use 
# the for loop to do so


# using a for loop instead to iterate through the list
for student in students:
    print(student)

#using length function to place studemts in rankings
for i in range(len(students)):
    print(i+1 , students[i])

    
#using dict to store students and their house
students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"}  
for student in students:
    print(student, students[student], sep=" is in ")


#lets try to add one more thing (their patronas)in our dict

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
for student in students:
    print (student["name"], student["house"], student["patronus"], sep=", ")
 