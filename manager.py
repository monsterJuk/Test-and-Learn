from person import Person


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, job='Manager', pay=pay)


    def giveRaise(self, persent, bonus=10):
        Person.giveRaise(self, persent + bonus)


if __name__ == '__main__':
    jorge = Manager('Jorge Lawrence', 100000)
    print(jorge)
    print(jorge.lastName())
    jorge.giveRaise(10, 10)
    print(jorge.pay)
    print(jorge)