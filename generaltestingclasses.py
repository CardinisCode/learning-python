class Furniture:
    def __init__(self, mat):
        self.actual_material = mat

    def print_material(self):
        print("I am made of", self.actual_material)

class Chair(Furniture):
    def __init__(self, mat="wood"):
        super().__init__(mat)

    def isSitable(self):
        return False

class SteelChair(Chair):
    def __init__(self):
        super().__init__("steel")

    def isSitable(self):
        return True

class WoodChair(Chair):
    def __init__(self):
        super().__init__("oak wood")
    
    def isSitable(self):
        return True

class Sofa(Furniture):
    def __init__(self):
        super().__init__("cloth")

"""
        F
      /    \
    C       S
   /  \ 
SC      WC
"""

furns = [
    #Furniture("no idea"), 
    Furniture(),
    Chair(), 
    SteelChair(), 
    WoodChair(),
    Sofa()
]

for f in furns:
    f.print_material()

    if isinstance(f, Chair):
        print("Chair is sitable:", f.isSitable())
    else:
        print("not a chair")
    