# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def sortNflatt(arr):
    result = sorted(sum(arr, []))
    print("The sorted and flattened list : " + str(result))

sortNflatt([[1,3],[2,3,4], [0,3,4]])


# Once a functional solution to this problem has been implemented, answer the following questions.
# How does this solution ensure data immutability?
 # it does not modify the original input, intead it creates a new list
# Is this solution a pure function? Why or why not?
 # Yes, it is. it does not  affect outside variables or have any side effects
# Is this solution a higher order function? Why or why not?
 # No, it doesnt tkae functions as arg or return a function as result
# Would it have been easier to solve this problem using a different programming style?
  # Every language or style are uniques, i believe it would be almost the same logic
# Why in particular is functional programming a helpful paradigm when solving this problem?
  # Use of pure functions & easier to read, this style is more concise & expresive


# Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

class Podracer:

    condition = ['perfect', 'trashed', 'repair']

    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        if self.condition == 'trashed':
            self.condition = 'repair'
            print('it has been repair')
        else: 
            print('Does not need a repair')

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed = self.max_speed * 2
        print(f'Your speed after boost is {self.max_speed}')

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self):
        self.condition = 'trashed'
        print('Now this needs a repair')

my_pod = Podracer(250, 'perfect', 100)
my_pod2 = Podracer(250, 'trashed', 100)

my_anakinsP = AnakinsPod(250, 'perfect', 100)

my_SebulbasP = SebulbasPod(250, 'perfect', 100)


my_pod.repair()
my_pod2.repair()

my_anakinsP.boost()
my_SebulbasP.flame_jet()

# Once an Object Oriented solution has been implemented, answer the following questions:
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation 
  # Methods & attributes inside a single class
    # max_speed, conditon, price inside of Podracer
# Abstraction
  # process of handling complexity by hiding unnecessary information from the user
    #  boost and flame_jet methods of the AnakinsPod abstract away the specific implementation details of how those operations are performed
# Inheritance
  # allows us to define a class that inherits all the methods and properties from another class.
    # AnkinsPod & SebulbasPod inherit from Podracer all the properties & methods , this allow to reuse existing code & funcitonality
# Polymorphism
  # defines methods in the child class that have the same name as the methods in the parent class
    # the use of the repair method in the Podracer override  the flame_jet method in the SebulbasPod class.
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
  # i repeat myself: Every language or style are uniques, i believe it would be almost the same logic
# How in particular did Object Oriented Programming assist in the solving of this problem?
  # allow us programmers to model real-world entities with attributes and behaviors, in the case of the Podracers problem, OOP was particularly helpful because it allowed to model the various aspects fo the Podracers as objects with specific properties and methods.