from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # str
        self.power = power  # int

    def run(self):
        print(f"Sir {self.name}, you are under attack!")
        enemies = 100
        day = 0
        while enemies > 0:
            enemies -= self.power
            day += 1
            sleep(1)
            print(f"{self.name} has been fighting for {day} days. There are {enemies} enemies left.")
            continue
        print(f"Sir {self.name} has won after {day} days!\n")


knight_1 = Knight('Jaime', 20)
knight_2 = Knight('Loras', 10)
knight_1.start()
knight_2.start()
knight_1.join()
knight_2.join()

print(f"The battle is over!")
