from .Apparaten import *


class Kamer:
    def __init__(self, naam: str):
        self.naam = naam
        self.apparaten_lijst: list[Apparaat] = []

    def voeg_apparaat_toe(self, apparaat:Apparaat):
        self.apparaten_lijst.append(apparaat)

 
    def __str__(self):
        return self.naam