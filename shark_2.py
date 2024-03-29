"""
    name: shark_2.py
    author: Jessica Soler
    created: 3/28/24
    assignment: 7.2 OOP Tutorial
    puprose: demonstrate object construction
"""

class Shark:
    """
        Initializes the shark object with two parameters
        If parameters are not passed in, the default values are used
    """
    
    def __init__(self, name="Name", age=0):
        self._name = name
        self._age = age
    
    # define shark methods
    def swim(self):
        print(f'{self._name} is swimming.')
        
    def be_awesome(self):
        print(f'{self._name} is being awesome.')
        
    def how_old(self):
        print(f'{self._name} is {self._age} years old.')
        
    # getters and setters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    
    def set_name(self, name):
        self._name = name
        
    def set_age(self, age):
        self._age = age
        
        
def main():
    
    # set name and age of Shark object during initialization
    sammy = Shark("Sammy", 2)
    sammy.how_old()
    sammy.be_awesome()
    
    # create another shark object with default values
    stevie = Shark()
    stevie.set_name("Stevie")
    stevie.set_age(1)
    stevie.how_old()
    stevie.swim()
    
# call the main method
if __name__ == "__main__":
    main()