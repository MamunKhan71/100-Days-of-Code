class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.color = kw.get("color")
        self.model = kw.get("model")
        self.nitro = kw.get("nitro")


cars = Car(nitro="True",color="Black")
print(cars.model)
