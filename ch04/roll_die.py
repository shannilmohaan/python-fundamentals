#roll_die.py
""" Roll a six sied die 6,000,000 times """
import random

#face frequency counters
face_1 = 0
face_2 = 0
face_3 = 0
face_4 = 0
face_5 = 0
face_6 = 0

#roll the die 6,000,000 times and count the occurences of each face.
for i in range(6_000_000): # used the _ here to make the number more readable.
    face = random.randrange(1,7)
    if face ==1:
        face_1 += 1
    elif face == 2:
        face_2 += 1
    elif face == 3:
        face_3 += 1
    elif face == 4:
        face_4 += 1
    elif face == 5:
        face_5 += 1
    elif face == 6:
        face_6 += 1

print (f'Face{"Frequency":>13}')
print(f'{1:<4}{face_1:>13}')
print(f'{2:<4}{face_2:>13}')
print(f'{3:<4}{face_3:>13}')
print(f'{4:<4}{face_4:>13}')
print(f'{5:<4}{face_5:>13}')
print(f'{6:<4}{face_6:>13}')
