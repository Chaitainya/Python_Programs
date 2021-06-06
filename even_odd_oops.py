# def evenodd(my_list):
#     even_list = []
#     odd_list = []
#     for numbers in my_list:
#         if numbers % 2 == 0:
#             even_list.append(numbers)
#         else:
#             odd_list.append(numbers)
#     return even_list
# num = evenodd([1,2,3,4,5,6,7,8,9,10])
# print(num)

my_list = [1,2,3,4,5,6,7,8,9,10]
class num_:
    def even(self):
        even_list = []
        for numbers in my_list:
            if numbers % 2 == 0:
                even_list.append(numbers)
        return even_list
    def odd(self):
        odd_list = []
        for numbers in my_list:
            if numbers % 2 != 0:
                odd_list.append(numbers)
        return odd_list

num = num_()
print(num.even())
print(num.odd())