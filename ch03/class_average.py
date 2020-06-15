#class_avergae.py
""" calculate the class avergae from a list of grades."""

grades_list = [98,76,71,87,83,90,57,79,82,94]
grade_total = 0
grade_counter = 0

#iterate through the grade list and compute total score and total number of grades

for grade in grades_list:
    grade_total += grade
    grade_counter += 1

#calculate class_average
class_average = grade_total/grade_counter
print(f'Class Average {class_average:>10.2f}')
