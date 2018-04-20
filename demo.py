class FlyBehavior():

    def fly(self):
        pass

    def eat(self):
        pass


class FlyNoway(FlyBehavior):

    def fly(self):
        print "i can't fly"

    def eat(self):
        print "i can't eat"

class Flyveryhigh(FlyBehavior):

    def fly(self):
        print "i can fly"



class Duck():

    def __init__(self,  behavior):
        self.flybehaviour = behavior()

    def performFly(self):
        self.flybehaviour.fly()

    def teach(self, newbehavior):
        self.flybehaviour = newbehavior()

woodenDuck = Duck(FlyNoway)
woodenDuck.performFly()
woodenDuck.teach(Flyveryhigh)
woodenDuck.performFly()

mallardDuck = Duck(Flyveryhigh)
mallardDuck.performFly()
