list_1 = [[1,2,3,],[4,5,6],[7,8,9,10]]
new_list = []
for sublist in list_1:
    for elements in sublist:
        new_list.append(elements)
print(new_list)

# List Comprehension
list_2 = [[1,2,3,],[4,5,6],[7,8,9,10]]
new_list_1 = [elements for sublist in list_2 for elements in sublist]
print(new_list_1)

# Function Programming
def list_(list_3):
    new_list_2 = []
    for sublist in list_3:
        for elements in sublist:
            new_list_2.append(elements)
    return new_list_2
print(list_([[1,2,3,],[4,5,6],[7,8,9,10]]))

# Function Programming with List Comprehensions
def list_22(list_4):
    new_list_3 = [elements for sublist in list_4 for elements in sublist]
    return new_list_3
print(list_22([[1,2,3,],[4,5,6],[7,8,9,10]]))