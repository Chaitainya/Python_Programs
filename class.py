class Cat:
    def __init__(self,name,breed,age):
        self.n = name
        self.b = breed
        self.a = age
cat_1 = Cat("Loki", "Persian", 2)
print("His name is",cat_1.n,",",cat_1.b,"cat and the age is",cat_1.a,"years old")
cat_2 = Cat("Kaleesi","Persian","2 months")
print("Her name is",cat_2.n,",",cat_2.b,"cat and the age is",cat_2.a,"years old")