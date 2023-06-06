
try:
    num_list = []
    num = int(input('Enter a list of numbers: '))
    for i in range(0,num):

    print(num_list)
except TypeError:
    print("It is a TypeEroor")
except ValueError:
    print('It is a ValueError')



#homework 1
#
# file_name = 'homework1.txt'
# try:
#     with open(file_name, 'r') as file2:
#         print(file2.read())
#         print('\n'  )
# except IOError:
#     print("IOError")

#homework 2

# import csv
#
# file_name1 = 'homework2_shopping.csv'
#
# fields = ['product', 'amount', 'price']
#
# rows = [['milk', '1', '0.98'],
#         ['bread', '1', '0.87'],
#         ['beer', '5', '1.29'],
#         ['coffee', '2', '2.39']]
#
# with open(file_name1, 'w') as csvfile:
#
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fields)
#     csvwriter.writerows(rows)
#     print('\n')
# with open(file_name1, 'r') as file3:
#     print(file3.read())
#     print('\n')
