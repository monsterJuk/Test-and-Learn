from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


    def lastName(self):
        return self.name.split()[-1]


    def giveRaise(self, persent):
        self.pay = int(self.pay * (1 + (persent / 100)))


if __name__ == '__main__':
    bob = Person('Bob Clark', 'Engeneer', 100000)
    
    print(bob)
    print(bob.lastName())
    bob.giveRaise(10)
    print(bob)
