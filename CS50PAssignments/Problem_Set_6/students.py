import csv

students = []

with open('students.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'name': row['name'], 'home': row['home']})

for student in students:
    print(f'{student["name"]} is form {student["home"]}')
