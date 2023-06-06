# Solved Exercises as home assignment for Lesson 3.

"""
name =  "Zeynep"
# print(name.count("e"))

# print(len(name))


shopping_list = ["tomatoes", "onions", "cucumbers", 52, [4, 8]]

shopping_set = {"tomatoes", "onions", "cucumbers", 52, 4, 8}


print(shopping_list)
print("\n")
shopping_list.pop(-2)
print(shopping_list)
print("\n")

list_from_set = list(shopping_set)
list_from_set.pop(-1)
print(list_from_set)
print("\n")
shopping_set.remove("onions")

print(shopping_set)

shopping_list.append("Curry")
print("\n")
print(shopping_list)

shopping_set.add("Milk")
print("\n")
print(shopping_set)

shopping_list.insert(2, "Juice")
print("\n")
print(shopping_list)

# shopping_list.add("Milk")
# print("\n")
# print(shopping_list)

list1 = ["Tomatoes", "milk", "Onions", "Juice", "Cucumbers"]
list2 = ["Juice", "Cucumbers", "Mango", 52]

list3 = []
for x  in list1:
    if x in list2:
        list3.append(x)

print(list3)


set1 = set(list1)
set2 = set(list2)
print("\n")
print(set1.intersection(set2))

car1 = {"Make": "Ford", "Model": "Mustang", "Year": 1969}

print("\n")

print(car1)

print("\n")

print(car1["Model"])

print(car1.get("Year"))

print(car1.values())

# car1.pop("Year")

# print(car1)

# del car1["Year"]
# print(car1)

car1["Year"] = 2019
print(car1)

car1.update({"Make": "BMW"})

print(car1)

# car1["Year"] = [2019, 2018, 2017]

# print(car1)


list1 = list(range(1,11))
print(list1)
print("\n")
z = []
for y in list1:
    if y % 2 != 0:
        z.append(y**2)
    else:
        z.append(y)

print(z)

z2 = [i**2 if(i % 2 != 0) else i^3 for i in list1 ]

#z2 = [i**2 if(i % 2 != 0) for i in list1 ]

print(z2)
"""
"""
set_1 = {"A","B","E","J","L", "O","K","Y","N"}
set_2 = {"c","B","D","N","P","Y","A","J","M"}
set_3 = set_1.union(set_2)
print(len(set_3))
print(set_1.intersection(set_2))
print(set_2.difference(set_1))
"""
"""
new_dict = {"Name": "xyz", "Age": "0"}
print("Previous", new_dict)
new_dict.update({"Name": "Sameer", "Age": 15})
print("After Update", new_dict)
"""
our_list = [x for x in range(1,101) if x%7==0]
print(our_list)
