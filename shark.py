"""
    name: shark.py
    author: Jessica Soler
    created: 3/28/24
    purpose: 7.1 OOP Tutorial
    demonstrate class, objects, methods
    getters and setters
"""

class Shark:
    """define shark methods"""
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
        
    def swim(self):
        print("The shark is swimming.")
        
    def be_awesome(self):
        print(f"{self._name} is being awesome.")
        
# create shark object
sammy = Shark()

# call shark methods
sammy.set_name("Sammy")
print(f"My name is {sammy.get_name()}")
sammy.swim()
sammy.be_awesome()