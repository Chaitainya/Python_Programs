def even(my_list):
    even_list = []
    for numbers in my_list:
        if numbers % 2 == 0:
            even_list.append(numbers)
    return even_list

def odd(my_list):
    odd_list = []
    for numbers in my_list:
        if numbers % 2 != 0:
            odd_list.append(numbers)
    return odd_list