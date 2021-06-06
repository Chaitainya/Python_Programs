# def add(x,y):
#     sum = 0
#     for i in my_list:
#         sum = sum + i
#     return sum
# print(add([1,2,3,4])) #We need to pass only twu numbers

# Functional Programming using args
def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(add(1,2,3,4))