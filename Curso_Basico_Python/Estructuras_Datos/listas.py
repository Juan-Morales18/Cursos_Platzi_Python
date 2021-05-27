
# Lists

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Hello', True]

print(my_list)

my_list.append('Juan')

print(my_list)

my_list.reverse()

print(my_list)

my_list.pop(0)

print(my_list)

for index, value in enumerate(my_list):
    print(index, value)

my_list2 = [10, 11, 12, 13, 14, 15]

for value_1, value_2 in zip(my_list, my_list2):
    print(value_1, value_2)
