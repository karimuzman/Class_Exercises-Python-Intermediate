#"Homework" solution
# 1. Write a function that returns true if a list is sorted.
def is_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True


# 2. Write a function that returns the first element that is not in the
# ascending order.
def find_not_sorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return lst[i]
    return None


# 3. Write a function that remove all elements that are not in the ascending
# order.
def remove_not_sorted(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] > lst[i]:
            lst.pop(i)
        else:
            i += 1


# 4. Write a function that move the out of order elements to other list.
def move_not_sorted(lst):
    new_list = []
    i = 1
    while i < len(lst):
        if lst[i - 1] > lst[i]:
            new_list.append(lst.pop(i))
        else:
            i += 1
    return new_list


print('Exercise 1. is_sorted:')

for fruits in [['apple', 'banana', 'cherry', 'eggplant'],  # sorted
               ['apple', 'banana', 'eggplant', 'cherry'],  # last one is wrong
               ['eggplant', 'cherry', 'banana', 'apple'],  # all reversed
               ['apple', 'apple', 'apple', 'apple'],  # all equal
               []]:  # empty case
    print("is_sorted(", fruits, ") =", is_sorted(fruits))

print()

print('Exercise 2. find_not_sorted:')

for numbers in [[1, 2, 4, 3, 5],  # simple case
                [5, 4, 3, 2, 1],  # reverse
                [1, 2, 3, 4, 5],  # sorted
                [1, 1, 1, 1, 1],  # all equal
                []]:  # empty
    print('find_not_sorted(', numbers, ') =', find_not_sorted(numbers))

print()

print('Exercise 3. remove_not_sorted:')

for numbers in [[1, 2, 4, 3, 5],  # simple case
                [5, 4, 3, 2, 1],  # reverse
                [1, 2, 3, 4, 5],  # sorted
                [1, 1, 1, 1, 1],  # all equal
                []]:  # empty case
    sorted_numbers = numbers.copy()
    remove_not_sorted(sorted_numbers)
    print('remove_not_sorted(', numbers, ') =', sorted_numbers)

print()

print('Exercise 4. move_not_sorted:')

for cars in [['audi', 'chevrolet', 'bmw', 'ford', 'honda', 'gmc'],  # simple case
             ['audi', 'honda', 'chevrolet', 'bmw', 'ford', 'gmc'],  # only two sorted
             ['audi', 'bmw', 'chevrolet', 'ford', 'gmc', 'honda'],  # all sorted
             ['honda', 'gmc', 'ford', 'chevrolet', 'bmw', 'audi']]:  # reversed
    sorted_cars = cars.copy()
    unsorted_cars = move_not_sorted(sorted_cars)
    print('cars         ', cars)
    print('sorted_cars  ', sorted_cars)
    print('unsorted_cars', unsorted_cars)
    print()
