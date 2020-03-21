class Counter:
    def __init__(self):
        self.count = 0

def incrementor(c, num):
    c.count = c.count + 1
    print("c.count:", c.count)
    num += 1

def main():
    counter = Counter()
    num = 0
    for x in range(0, 100):
        incrementor(counter, num)
        
    return (counter.count, num)

aTuple = main()


class Name: 
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Person:
    def __init__(self, name, eyecolour, age):
        self.name = name
        self.eyecolour = eyecolour
        self.age = age


myPerson = Person(Name("John", "Smith"), "brown", 32)
print(myPerson.name.firstname)
print(myPerson.age)
    