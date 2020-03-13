class Dog: 
    def __init__(self, name = " ", owner=None):
        self.name = name
        self.owner = owner
    def speak(self):
        print("Woof!")

class Owner: 
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("My name is:", self.name)

owner1 = Owner("David")
owner2 = Owner("Priyank")
dog1 = Dog("Fido", owner1)
dog2 = Dog("Barkley", owner2)
dog3 = Dog("Spot", owner2)
dog4 = Dog()
newList = [owner1, dog1, owner2, dog2, dog3, dog4]
for item in newList:
    print(item.speak())
    