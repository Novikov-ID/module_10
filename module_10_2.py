import threading
from time import sleep


class Knight(threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        days = 0
        while self.enemies > 0:
            self.enemies = self.enemies - self.power
            days += 1
            print(f'{self.name} сражается {days} день(дня)..., осталось {self.enemies} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')