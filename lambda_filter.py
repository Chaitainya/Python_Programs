# Lambda functions using filter on even numbers
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = list(filter(lambda x : x % 2 == 0, my_list))
print(new_list)

my_tuple = (1,2,3,4,5,6,7,8,9,10)
new_tuple = tuple(filter(lambda x : x % 2 == 0, my_tuple))
print(new_tuple)

# odd numbers
my_list1 = [1,2,3,4,5,6,7,8,9,10]
new_list1 = list(filter(lambda x : x % 2 == 1, my_list1))
print(new_list1)

my_tuple1 = (1,2,3,4,5,6,7,8,9,10)
new_tuple1 = tuple(filter(lambda x : x % 2 == 1, my_tuple1))
print(new_tuple1)