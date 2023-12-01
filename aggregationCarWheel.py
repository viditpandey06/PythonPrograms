class Wheel:
    def __init__(self, brand, warranty):
        self.brand = brand
        self.warranty = warranty

    def get_wheel_info(self):
        return f"Wheel Brand: {self.brand}, Warranty: {self.warranty} months"


class Car:
    def __init__(self, model, speed, color, wheel):
        self.model = model
        self.speed = speed
        self.color = color
        self.wheel = wheel  

    def get_car_info(self):
        return f"Model: {self.model}, Speed: {self.speed} mph, Color: {self.color}\nWheel Info: {self.wheel.get_wheel_info()}"



wheel1 = Wheel("XYZ Wheels", 24)  


car1 = Car("Sedan", 120, "Blue", wheel1)


print(car1.get_car_info())
