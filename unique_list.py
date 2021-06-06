list_ = [1,2,3,4,4,4,4,5,6,7,8,9]
unique_list = []
for i in list_:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

# functionalu programming
def unique_numbers(my_list):
    unique_list = []
    for number in my_list:
        if number not in unique_list:
            unique_list.append(number)
    return unique_list
print(unique_numbers([1,2,3,4,4,4,4,5,6,7,8,9]))