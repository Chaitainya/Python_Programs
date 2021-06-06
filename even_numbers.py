# Generic Python
my_list = [1,2,3,4,5,6,7,8,9,10]

even_list = []
for i in my_list:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

# Functional Programming
def numbers(my_list_1):
    even_ = []
    for i in my_list:
        if i % 2 == 0:
            even_.append(i)
    return even_
print(numbers([1,2,3,4,5,6,7,8,9,10]))

# List Comprehensions
my_list_2 = [1,2,3,4,5,6,7,8,9,10]
even_num = [i for i in my_list_2 if i % 2 == 0]
print(even_num)