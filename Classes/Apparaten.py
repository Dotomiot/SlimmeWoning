class Apparaat:
    def __init__(self):
        self.statusAan = False

    def pasStatusAan(self, status):
        self.statusAan = status

class Lamp(Apparaat):
    def __init__(self, helderheid=0):
        super().__init__()
        self.helderheid = helderheid


    def veranderHelderheid(self, helderheid):
        if helderheid > 100:
            helderheid = 100
        self.helderheid = helderheid
    
    def __str__(self):
        if self.statusAan == True:
            return f"Mijn helderheid is {self.helderheid}% en ik sta aan"
        else:
            return f"Mijn helderheid is {self.helderheid}% en ik sta uit"
    
lama = Lamp(20)
print(lama.helderheid)
print(lama.statusAan)

print(lama)

lama.veranderHelderheid(69)
lama.pasStatusAan(True)

print(lama.helderheid)
print(lama.statusAan)

print(lama)