class vehicle:
    def __init__(self,name,number = 28):
        self.name = name
        self.number = number
    def getcarname(self):
        print(self.name)

class suv(vehicle):
    def __init__(self,name,number=28):
        super().__init__(name,number)
    def getsuv(self,number):
        print("suv",self.name)
        print(self.number)
        super().__init__(self.name,number)
        print(self.number)
    

car = suv("abc")
# car.vehicle("abc")
car.getsuv(50)
car.getcarname()