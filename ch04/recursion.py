#fatorial.py
""" compute the factorial by calling a recursive function"""

def factorial(number):
    """Return factorial of a number"""
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


for i in range(11):
    print(f'{i:<3}!= {factorial(i):>6}')
