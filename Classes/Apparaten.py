class Apparaat:
    def __init__(self):
        self.statusAan = False

    def pas_status_aan(self, status):
        self.statusAan = status

class Lamp(Apparaat):
    def __init__(self, helderheid=0):
        super().__init__()
        self.helderheid = helderheid


    def verander_helderheid(self, helderheid):
        if helderheid > 100:
            helderheid = 100
        self.helderheid = helderheid
    
    def __str__(self):
        if self.statusAan == True:
            return f"Mijn helderheid is {self.helderheid}% en ik sta aan"
        else:
            return f"Mijn helderheid is {self.helderheid}% en ik sta uit"

class Thermostaat(Apparaat):
    def __init__(self, temperatuur=0):
        super().__init__()
        self.temperatuur = temperatuur


    def verander_temperatuur(self, temperatuur):
        if temperatuur > 100:
            temperatuur = 100
        self.temperatuur = temperatuur

    def temperatuur(self):
        return self.temperatuur
    
    def __str__(self):
        if self.statusAan == True:
            return f"Mijn temperatuur is {self.temperatuur}% en ik sta aan"
        else:
            return f"Mijn temperatuur is {self.temperatuur}% en ik sta uit"
    
class Deurslot(Apparaat):
    def __init__(self, dicht=True):
        super().__init__()
        self.statusAan = dicht
    
    def __str__(self):
        if self.statusAan == False:
            return f"Ik ben open"
        else:
            return f"Ik ben op slot"
    
class Bewegingssensor(Apparaat):
    def __init__(self):
        super().__init__()
        self.statusAan = False
        
    def detecteer(self):
        self.statusAan = not self.statusAan

class Rookmelder(Apparaat):
    def __init__(self):
        super().__init__()
        self.statusAan = False
        self._fireDetectionThreshold = 69
        self.fireDetection = 0

    def detectFire(self, firePercentage):
        self.fireDetection = firePercentage
        if firePercentage >= self._fireDetectionThreshold:
            print(f"VUUR! ER IS BRAND! PASUIT!")
        else:
            print(f"Er is geen vuurdetectie")

class Gordijn(Apparaat):
    def __init__(self):
        super().__init__()

    

def main():
    lama = Lamp(20)
    print(lama.helderheid)
    print(lama.statusAan)

    print(lama)

    lama.verander_helderheid(69)
    lama.pas_status_aan(True)

    print(lama.helderheid)
    print(lama.statusAan)

    print(lama)


if __name__ == "__main__":
    main 