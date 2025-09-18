class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
        
    def sip(self):
        print("Sipping the chai...")
        
    def add_sugar(self, amount):
        print("Adding sugar...")
        
my_chai = Chai(sweetness=5, milk_level=3)

my_chai.add_sugar(2)
my_chai.sip()
