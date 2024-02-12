from person import Person
from manager import Manager

if __name__ == '__main__':
    bob = Person('Bob Clark', 'Engeneer', 100000)
    jorge = Manager('Jorge Lawrence', 100000)
    print(bob)
    print(jorge)
    for i in (bob, jorge):
        i.giveRaise(10)
        print(i.lastName())
    print(bob)
    print(jorge)
    