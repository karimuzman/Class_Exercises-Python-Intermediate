# Solved Exercises as home assignment for Lesson 1.
def num (x, y):
    result = (x+2)*(y-3)
    return result

print (num(2, 2))


def is_negative (value):
    if value < 0:
        print("The result is negative!")
        c = num(2, 2)
        print("c = ", c)
is_negative(num(2, 2))


def hallo(name):
    greeting_msg = f"Hello!!! {name}"
    print(greeting_msg)

name = input("What is your Name: ")
hallo(name)

def mul (x,y):
    result = (x*y)
    return result


num1 = int(input("Enter ths first value: "))
num2 = int(input("Enter ths second value: "))
print(mul(num1,num2))