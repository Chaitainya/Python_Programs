class Add:
    
    num_1 = 4
    num_2 = 5

    def __init__(self,num_3):
        self.num_3 = num_3

    def num(self):
        return self.num_1 + self.num_2 + self.num_3

add = Add(6)
print(add.num())