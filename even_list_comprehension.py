# List Comprehension with functional programming
def numbers(my_list_2):
    even_num = [i for i in my_list_2 if i % 2 == 0]
    return even_num
print(numbers([1,2,3,4,5,6,7,8,9,10]))