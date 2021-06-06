# def greet(names):
#     for name in names:
#         print("Hello", name)
# greet("monica")

def greet(*names):
    for name in names:
        print("Hello", name)
greet("monica","leon","sheema")