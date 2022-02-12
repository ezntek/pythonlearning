
# class Human
class Human:
    def __init__(self,age,name):
        self.age = None
        self.name = None
        self.hunger = 0
    
    def eat(self):
        if self.hunger > 9:
            print("Human ate food and is less hungry")
            self.hunger -= 10
        else:
            print("It isn't hungry, so human did not eat anything.")
        # end if
        # end def

    def hello(self):
        print("hello from human")
    # end def
# end class

# Main
person = Human(13,"person")
person.hello()
#end main