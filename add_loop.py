l = [1,2,3,4]
sum = 0
for i in l:
    sum = sum + i
print(sum)

sum = 0
for i in range(100):
    sum = sum + i
print(sum)

sum = 0
for i in range(0,100,10):
    sum = sum + i
print(sum)

# Functional Programming
def add(my_list):
    sum = 0
    for i in my_list:
        sum = sum + i
    return sum
print(add([1,2,3,4]))

# list_ = []
# for i in range(0,100,10):
#     list_.append(i)
# print(list_)