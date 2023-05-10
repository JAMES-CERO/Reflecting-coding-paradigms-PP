# Implement a function that will flatten and sort an array of integers 
# in ascending order, and which adheres to a functional programming paradigm.

def sortNflatt(arr):
    result = sorted(sum(arr, []))
    print("The sorted and flattened list : " + str(result))

sortNflatt([[1,3],[2,3,4], [0,3,4]])



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

