# This is place to know Inheritance in Python
class father:
    def __init__(self, blood):
        self.money = 1000
        self.blood = blood

class son(father):
    def __init__(self, blood, hobby):
        super().__init__(blood)
        self.hobby = hobby

class daughter(father):
    money = 0
    
s = son("A","play game")
d = daughter("B")
print("Son has", s.money)
print("Son Blood", s.blood)
print(s.__dict__)
print("Daughter has", d.money)
print("Daughter Blood", d.blood) 