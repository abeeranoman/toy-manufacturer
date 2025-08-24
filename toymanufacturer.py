#A toy manufacturer makes cuddly toys of four types in three sizes. 
# Some toys are teddy bears, and some are bunny rabbits. Blue teddy bears are dressed as engine drivers. and red ones as gardeners
# . White bunnies are dressed as clowns, and black ones as bank managers. Teddies make a growling noise, whereas bunny rabbits squeak. 
# All toys can say what job they do, what their colour is and what size they are.


#IMPORTANT NOTe: This file is specifically for practice and is not based on the actual QUESTION, but merely the intial DESCRIPTION 
class Teddy:
    noise = "Growl"

    def colour(self, colour):
        colour = colour.strip().lower()    #We typed strip() to utterly abolish any spaces like if " red " then it'll convert it to "red"
                                            # then lower() to convert the users input whether it be Red or rEd or RED
        allowed_colours = ["blue", "red"]  #we made sure to write blue and red in lower case since we used lower() and in order for it to work 
                                            #we have to use lower case in  our method.
        if colour not in allowed_colours:
            raise ValueError("We have no other colours available at the moment")
        self.colour = colour  

#if red is the colour then it further determines the job 
        if self.colour == "red":
            self.job = "Engine Driver"
        elif self.colour== "blue":
            self.job = "Gardener"
        
        else:
            raise ValueError 
        
    def size(self, size):
        size = size.strip().lower()
        self.size = size 
        allowed_size = ["large", "small", "medium"]
        if size not in allowed_size:
            raise ValueError("There is no such size avialable")
        
        print (f"Hi! I am a {self.colour} teddy! I am a {self.job}, and my size is: {self.size}. I can {self.noise} too!")


v1 = Teddy()
v1.colour("Blue")
v1.size("Large")

v2 = Teddy()
v2.colour("Red")
v2.size("Small")



class Bunny:
    noise = "Squeak"

    def colour (self, colour):
        colour = colour.strip().lower()
        self.colour = colour
        allowed_colours = ["white", "black"]
        if colour not in allowed_colours: 
            raise ValueError ("Sorry, this colour isn't available at the moment")
    

        if self.colour == "white":
            self.job = "Clown"
        if self.colour == "black":
            self.job = "Bank Manager"

    def size(self, size):
            size = size.strip().lower()
            self.size = size 
            allowed_sizes = ["large", "medium", "small"]
            if size not in allowed_sizes:
                raise ValueError ("This size isn't available at the moment")
            
            print (f"Hi! I am a {self.colour} bunny! I am a {self.job}, and my size is: {self.size}. I can {self.noise} too!")



v1 = Bunny()
v1.colour("white")
v1.size("Large")

v2 = Bunny()
v2.colour("black")
v2.size("Small")


