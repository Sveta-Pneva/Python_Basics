from time import sleep
class TrafficLight:
    __states = {'red': 7, 'yellow': 2, 'green': 21}
    __color = ''
    rounds = 3
    def running(self):
        for i in range(self.rounds):
            for color, time in self.__states.items():
                self.__color = color
                print(color)
                sleep(time)

traffic_light = TrafficLight()
traffic_light.running()
