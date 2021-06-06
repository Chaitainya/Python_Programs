list_1 = [1,5,6]
list_2 = [7,8,6]
new_list = []
for i, j in zip(list_1, list_2):
    if i == j:
        new_list.append(i)
print(new_list)