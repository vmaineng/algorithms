class Car:
    def __init__(self, make, model):
        #special method that is a constructor that initializes object
        #with specific variables to use immediately
        self.make = make
        self.model = model

car1 = Car('Honda', "Civic")

print(car1.make)
print(car1.model)