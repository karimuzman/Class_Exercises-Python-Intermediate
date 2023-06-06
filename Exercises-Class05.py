#1. Generate 10 random floating point numbers between 0 and 100, round them to 2 decimal points.

from random import random
rand_num = [round(random()*100, 2) for _ in range(10)]
print(rand_num)

#2. Calculate the product of all the numbers in a list.

def multiplylist(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result

product_num = [1,2,3,4,5,6]
print(multiplylist(product_num))

#3. Find the longest string in a list.

words = ["apple", "banana", "cat", "dog", "elephant", "fire", "giraffe", "hippopotamus", "igloo",
"jaguar", "kangaroo", "lemur", "monkey", "noodles", "octopus", "pizza"]

longest_string = max(words, key=len)
print(longest_string)

num_list = [1, 2, 3, 4, 3, 2, 1]
for n in num_list:
    print("*" * n)



