# Solved Exercises as home assignment for Lesson 2.

def first_occ(x):
    
    x = "The worlds fastest plane"
    return x

a = input("Which substring you want to find :")
print(first_occ(a).find(a))


num = int(input("Enter a natural number to calculate sum:"))
hold = num
sum = 0

if num <= 0:
    print("Enter a whole positive number!")
else:
    while num > 0:
        sum = sum + num
        num = num -1
    print ("Sum of first", hold, "natural numbers is", sum)


i = 1
while i < 11:
    print (i)
    i += 1


"""
def cal_bmi(x, y):
    result = (y/x**2)
    return result

num1 = float(input("Enter your height in meters: "))
num2 = float(input("Enter your weight in Kgs: "))
print(cal_bmi(num1,num2))
"""