#mask_minors_age.py
""" Read the age from a list and mask the age of a minor with 'minor' value """

#define ages in a list
age_list = [35,9,12,45,89,99,67,10,13,15,87,18,13]
print("Before masking",age_list)

#iterate through the list and mask the minor's age with value 'minor'
for i,age in enumerate(age_list):
    if age < 18:
        is_minor = True
        age_list[i] = 'minor'
print("After masking",age_list)
