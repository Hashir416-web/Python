class vehicile:
    def __init__(self,name ,mileage, speed):
        self.name = name
        self.mileage = mileage
        self.speed = speed
class bus(vehicile):
    pass
school_bus = bus("Volovo", 18000, 180)
print("Vehicle Name:", school_bus.name, "and the speed is:", school_bus.speed,"and the mileage is:", school_bus.mileage)