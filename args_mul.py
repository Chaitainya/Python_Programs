def mul(*args):
    result = 1
    for number in args:
        result = result * number
    return result
print(mul(1,2,3,4,5,6,7,8,9))
