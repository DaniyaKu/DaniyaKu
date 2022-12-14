import itertools
import sys

class fibonat:
    class _fibonat_iter:
        def __init__(self):
            self.previous = 1  
            self.now = 1 
            self.next = 0  
            self.counter = 0

        def __next__(self):
            self.counter += 1
            if self.counter == 1 or self.counter == 0:
                return 1 
            self.next = self.previous + self.now
            self.previous = self.now
            self.now = self.next
            return self.now

    def __iter__(self):
        return fibonat._fibonat_iter()

def print_fibonat(amount: int):
    assert amount > 0, 'Не получится('
    to_print = fibonat()
    for i in itertools.islice(to_print, amount):
        print(i)

def go_input():
    amount = input('Сколько чисел вывести? \n')
    return amount

try:
    amount = int(go_input())
    print_fibonat(amount)
except:
    print('Некорректный ввод!')
    sys.exit()
