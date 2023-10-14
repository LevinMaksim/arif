f = open('students.txt' , 'r' , encoding='utf-8')
students = []
for student_str in f:
    s = student_str.split(';')
    students.append({'id': int(s[0]), 'full_name': s[1], 'gender': s[2], 'variant': int(s[3])})

f.close()

surname = input('Введите фамилию: ')

for student in students:
    if student['full_name'].split()[0] == surname:
        print(student)





'''
stud_list1 = stud1.split(';')
stud_list2 = stud2.split(';')
stud_list3 = stud3.split(';')

stud_dict_1 = {'name': stud_list1[1], 'surname': stud_list1[0], 'patr': stud_list1[2]}
stud_dict_2 = {'name': stud_list2[1], 'surname': stud_list2[0], 'patr': stud_list2[2]}
stud_dict_3 = {'name': stud_list3[1], 'surname': stud_list3[0], 'patr': stud_list3[2]}

students = []
students.append(stud_dict_1)
students.append(stud_dict_2)
students.append(stud_dict_3)

print(students)
'''
