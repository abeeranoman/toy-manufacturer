#Model the classes as described above in a hierarchy, the highest level of which should be the base class 'Cuddly Toy'. 
# 'There should be, an intermediate level of classes Teddy' and 'Bunny', and at the lowest level classes of 'engine driver, 'gardener', 'clown' and 'bank manager'. Instantiate objects of these classes dynami-cally via a base class pointer, setting the size of the toy via a parameter to the constructor. 
# Use class attributes as appropriate.
#  Demonstrate a method which wallows the toy to make a noise and tell us about itself



#Highest Class:

class CuddleToys:
    def __init__(self, size):
        size = size.strip().lower()
        self.size = size 
        allowed_size = ["large", "small", "medium"]
        if size not in allowed_size:
            raise ValueError("There is no such size avialable")
        
    def talk(self):
        parent_class = self.__class__.__bases__[0].__name__    #bases keeps a track of the parent class and [0] just gives us the first parent class
        print (
            f"Hi! I am a {self.colour} {parent_class}!"
               f" I am a {self.job}, and my size is: {self.size}. I can {self.noise} too!"
               )
        
#Intermediate Class:

class Teddy(CuddleToys):
    noise = "Growl"

class Bunny(CuddleToys):
    noise = "Squeak"

#Lower class:

class EngineDriver(Teddy):
    def __init__(self,size):
        super().__init__(size)   #we used super(). for engine driver to directly inherit the size from the parent_class (Teddy, in this case)
        
        self.colour = "blue"
        self.job = "Engine Driver"

class Gardener(Teddy):
    def __init__(self, size):
        super().__init__(size)
        
        self.colour = "red"
        self.job = "Gardener"

class BankManager(Bunny):
    def __init__(self, size):
        super().__init__(size)
        
        self.colour = "black"
        self.job = "Bank Manager"

class Clown(Bunny):
    def __init__(self, size):
        super().__init__(size)
        
        self.colour = "white"
        self.job = "Clown"

