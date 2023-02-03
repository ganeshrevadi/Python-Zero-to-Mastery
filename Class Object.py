class PlayerChar:
    #Class object attribute
    membership =  True

    def __init__(self,name='noname',age=0):
        self.name = name #attributes
        self.sge = age
    
    def shout(self):
        print(f'My name is {self.name}')
        pass
    
    @classmethod
    def add(cls,num1 ,num2):
        return num1+num2

    @staticmethod
    def add(num1 , num2):
        return num1 + num2

p1 = PlayerChar("Akhmood", 19) #instance
p2 = PlayerChar()

print(p2)
print(p2.name)

print(p1.name)
print(p1.membership)
print(p1.shout())

print(PlayerChar.add(5,6))

