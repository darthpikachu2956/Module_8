import random, time, queue
from threading import Thread


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        x = random.randint(3, 10)
        time.sleep(x)


class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):  # неограниченное кол-во гостей (объектов класса Guest)
        for g in guests:
            assigned = False
            for t in self.tables:
                if t.guest is None:
                    t.guest = g
                    g.start()
                    print(f"{g.name} has taken the table number {t.number}.")
                    assigned = True
                    break
            if not assigned:
                self.queue.put(g)
                print(f"{g.name} is in queue.")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} has finished and left.")
                    print(f"The table number {t.number} is free.")
                    t.guest = None
                if t.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    t.guest = next_guest
                    print(f"{next_guest.name} left the queue and took the table number {t.number}.")
                    next_guest.start()
            time.sleep(1)


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

