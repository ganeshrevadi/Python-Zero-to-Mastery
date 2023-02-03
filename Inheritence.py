class User:
    def login(self):
        print("Logged IN")
    
    def attack(self):
        print(f'attacking by {self.name}')

class Wizard(User):
    def __init__(self,name):
        self.name = name 


w1 = Wizard('Merlin')

print(w1.login())
print(w1.attack())