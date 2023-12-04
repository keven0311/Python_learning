# students = ['Hermione', 'Harry', 'Ron']

# for i in range(len(students)):
#     print(i+1, students[i])
    
    
# students = {'Hermione':'Gryffindor', 
#             'Harry':'Gryffindor',
#             'Ron':'Gryffindor',
#             'Draco':'Slytherin'
#             }

# for student in students:
#     print(student, students[student], sep=',')

# print(students.values())

theG = 'Gryffindor'
theS = 'Slytherin'

students = [
    {"name":'Hermione', 'house':theG, 'patronus':'Otter'},
    {"name":'Harry','house':theG, 'patronus':'Stag'},
    {"name":'Ron','house':theG, 'patronus':'Jack Russell terrier'},
    {"name":'Draco','house':theS, 'patronus':None},
    
]

for student in students:
    print(student['name'],student['house'], student['patronus'], sep= ', ')