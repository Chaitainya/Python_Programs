# x = int(input("Enter the number: "))
# for i in range(1, 13):
#     print(x, "X", i, "=", x * i)

# Using lambda function in functional programming
def table(n):
    return lambda a : a * n
n = int(input("Enter the number: "))
b = table(n)
for i in range(1,11):
    print(n, "X", i, "=", b(i))