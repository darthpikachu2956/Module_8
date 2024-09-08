# Задача "Банковские операции"
import threading as t
import time
import random as r


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = t.Lock()

    def deposit(self):
        for i in range(1, 11):
            x = r.randint(50, 500)
            self.balance += x
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            print(f"\nDeposit: {x}$. Current balance: {self.balance}$.")
            time.sleep(1)

    def take(self):
        for j in range(1, 11):
            y = r.randint(50, 500)
            print(f"\nRequest to get {y}$.")
            if y <= self.balance:
                self.balance -= y
                print(f"Taking: {y}$. Current balance: {self.balance}$.")
            else:
                print(f"Request denied: not enough money.")
                self.lock.acquire()
            time.sleep(1)


lolbank = Bank()
thr1 = t.Thread(target=Bank.deposit, args=(lolbank,))
thr2 = t.Thread(target=Bank.take, args=(lolbank,))
thr1.start()
thr2.start()
thr1.join()
thr2.join()
print(f"\nThe final result on balance: {lolbank.balance}$.")
