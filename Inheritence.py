class User:
    def login(self):
        print("Logged IN")
    
    

class Wizard(User):
    def __init__(self,name,power):
        self.name = name 
    
    def attack(self):
        print(f'attacking by {self.name}')


class Archer(User):
    def __init__(self, name , arrows):
        self.name = name 
        self.arrows = arrows

    def check(self):
        print(f'There are {self.arrows}  arrows remaining')

w1 = Wizard('Merlin',50)

class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('borgie', 50, 100)
print(hb1.login())
