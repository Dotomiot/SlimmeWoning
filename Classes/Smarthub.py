from __future__ import annotations  # nodig voor string type hints als "Woning"
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Woning import Woning
    from .Apparaten import *
    from .Kamer import Kamer

def regels(apparaat: Apparaat, helderheid=100, temperatuur = 23, slot=True, other=True, detection=False):
    # print(type(apparaat), end=", ")
    # print(str(type(apparaat)).find("Lamp"), end=", ")
    # print(str(type(apparaat)).find("Deurslot"), end=", ")

    if str(type(apparaat)).find("Lamp") == 26:
        lamp:Lamp = apparaat

        lamp.statusAan = True
        lamp.verander_helderheid(helderheid)

    elif str(type(apparaat)).find("Thermostaat") == 26:
        thermostaat:Thermostaat = apparaat

        thermostaat.statusAan = True
        thermostaat.verander_temperatuur(temperatuur)

    elif str(type(apparaat)).find("Deurslot") == 26:
        deurslot:Deurslot = apparaat

        deurslot.statusAan = slot

    elif str(type(apparaat)).find("Beweging") == 26:
        bewegingssensor:Bewegingssensor = apparaat

        bewegingssensor.statusAan = detection

    elif str(type(apparaat)).find("Rook") == 26:
        rookmelder:Rookmelder = apparaat

        rookmelder.statusAan = True

    elif str(type(apparaat)).find("Gordijn") == 26:
        gordijn:Gordijn = apparaat

        gordijn.statusAan = other



class Smarthub():
    def __init__(self, naam="Smarthub"):
        self.subcribtion_topic_list = []
        self.subcribtions = {}
        self.naam = naam

    def subscribe(self, topic):
        self.subcribtion_topic_list.append(topic)

    def recieve_mqtt(self, topic, data):
        self.subcribtions[topic] = data

    def voer_regel_uit(self, woning: Woning, kamer: int, vorige_kamer: int, scenario=1):

        kamer: Kamer = woning.kamers[kamer]
        vorige_kamer: Kamer = woning.kamers[vorige_kamer]

        for apparaat in kamer.apparaten_lijst:

            if scenario == 1: # default
                regels(apparaat, detection=True)
            elif scenario == 2: # nacht
                regels(apparaat, 25, 18, True, False, True)
            # elif scenario == 3: # vakantie


        for apparaat in vorige_kamer.apparaten_lijst:

            if scenario == 1: # default
                regels(apparaat, 0, 20, True, False)
            elif scenario == 2: # nacht
                regels(apparaat, 0, 18, True, False)
