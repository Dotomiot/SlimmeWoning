from .Kamer import Kamer

class Woning():
    def __init__(self,naam="Huis"):
        self.kamers: list[Kamer] = []
        self.naam = naam

    def voeg_kamer_toe(self, kamer:Kamer):
        self.kamers.append(kamer)

# def main():
#     kamer1 = Kamer("slaap")
#     lampje = Lamp(50)
#     slot = Deurslot(True)
#     kamer1.voeg_apparaat_toe(lampje)
#     kamer1.voeg_apparaat_toe(slot)
#     kamer2 = Kamer("bad")
#     kamer3 = Kamer("keuken")
#     woning1 = Woning()
#     woning1.voeg_kamer_toe(kamer1)
#     woning1.voeg_kamer_toe(kamer2)
#     woning1.voeg_kamer_toe(kamer3)

#     for kamer in woning1.kamers:
#         print(kamer.naam)
#         for apparaat in kamer.apparaten_lijst:
#             print(apparaat)


# if __name__ == "__main__":
#     main()