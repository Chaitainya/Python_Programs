class Car:

    def __init__(self,company,model,color):
        self.c = company
        self.m = model
        self.co = color

    def getModel(self):
        return self.m

    def getCompany(self):
        return self.c

    def getColor(self):
        return self.co

    def setColor(self,color):
        self.co = color

class Vehicle(Car):

    def __init__(self,company,model,color,variant):
        super().__init__(company,model,color)
        self.v = variant

    def info(self):
        return self.c + " " + self.m + " " + self.co + " " + self.v

car = Car("BMW",2021,"Black")
print(car.c)
print(car.m)
print(car.co)

car.setColor("Red")
print(car.co)

vehicle_1 = Vehicle("BMW","2021","Green","6Seater")
print(vehicle_1.info())