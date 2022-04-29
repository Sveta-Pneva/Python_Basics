class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} go'
    def stop(self):
        return f'{self.name} stop'
    def turn(self, direction):
        self.direction = direction
        if 'r' in direction:
            return f'{self.name} turn right'
        else:
            return f'{self.name} turn left'
    def show_speed(self):
        return f'{self.name} speed: {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} - fast speed({self.speed})'
        else:
            return f'{self.name} - normal speed({self.speed})'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} - fast speed({self.speed})'
        else:
            return f'{self.name} - normal speed({self.speed})'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
jaguar = SportCar(100, 'Black', 'Jaguar', False)
volkswagen = TownCar(30, 'White', 'Volkswagen', False)
kia = WorkCar(70, 'Grey', 'Kia', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(kia.turn("left"))
print(volkswagen.turn("right"))
print(kia.go())
print(ford.name, ford.color)
print(jaguar.name, jaguar.is_police)
print(ford.name, ford.is_police)
print(ford.stop())
print(volkswagen.show_speed())
print(kia.show_speed())