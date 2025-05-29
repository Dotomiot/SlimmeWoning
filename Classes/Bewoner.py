from .Kamer import Kamer
from random import randint

class Bewoner():
    def __init__(self, naam):
        self.naam = naam
        self.huidigeKamer = "none"
        self.huidigeKamerInt = 0
        self.vorigeKamerInt = 1

    def beweeg_bewoner(self, nieuwe_kamer):
        self.huidigeKamer = nieuwe_kamer

    def beweeg_bewoner(self, kamerlijst: list[Kamer]):
        self.vorigeKamerInt = self.huidigeKamerInt

        # Niet dezelfde kamer gekozen
        looping = True
        while looping:
            rng = randint(0, len(kamerlijst)-1)

            if rng != self.huidigeKamerInt:
                self.huidigeKamerInt = rng
                looping = False

        # Wel dezelfde kamer mogelijk:
        # rng = randint(0, len(kamerlijst)-1)

        self.huidigeKamer = kamerlijst[rng]
        return self.huidigeKamer


def main():
    test = randint(0,1)
    print(test)


main()