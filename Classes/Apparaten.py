class Apparaat:
    def __init__(self):
        statusAan = False

    def pasStatusAan(self, status):
        self.statusAan = status

class Lamp(Apparaat):
    def __init__(self):
        helderheid = 0

    def veranderHelderheid(self, helderheid):
        if helderheid > 100:
            helderheid = 100
        self.helderheid = helderheid
    