from __future__ import annotations  # nodig voor string type hints als "Woning"
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Woning import Woning
    from .Apparaten import *
    from .Kamer import Kamer

class Smarthub():
    def __init__(self, naam="Smarthub"):
        self.subcribtion_topic_list = []
        self.subcribtions = {}
        self.naam = naam

    def subscribe(self, topic):
        self.subcribtion_topic_list.append(topic)

    def recieve_mqtt(self, topic, data):
        self.subcribtions[topic] = data

    def voer_regel_uit(self, woning: Woning, kamer: int, vorige_kamer: int):
        # print(kamer, end="\t")
        # print(vorige_kamer, end="\t")

        kamer: Kamer = woning.kamers[kamer]
        vorige_kamer: Kamer = woning.kamers[vorige_kamer]

        for apparaat in kamer.apparaten_lijst:
            # print(type(apparaat), end=", ")
            # print(str(type(apparaat)).find("Lamp"), end=", ")
            # print(str(type(apparaat)).find("Deurslot"), end=", ")


            if str(type(apparaat)).find("Lamp") == 26:
                lamp:Lamp = apparaat

                lamp.statusAan = True
                lamp.verander_helderheid(100)

            elif str(type(apparaat)).find("Thermostaat") == 26:
                thermostaat:Thermostaat = apparaat

                thermostaat.statusAan = True
                thermostaat.verander_temperatuur(23)

            elif str(type(apparaat)).find("Deurslot") == 26:
                deurslot:Deurslot = apparaat

                deurslot.statusAan = False

            elif str(type(apparaat)).find("Beweging") == 26:
                bewegingssensor:Bewegingssensor = apparaat

                bewegingssensor.statusAan = True

            elif str(type(apparaat)).find("Rook") == 26:
                rookmelder:Rookmelder = apparaat

                rookmelder.statusAan = True

            elif str(type(apparaat)).find("Gordijn") == 26:
                gordijn:Gordijn = apparaat

                gordijn.statusAan = True

        for apparaat in vorige_kamer.apparaten_lijst:
            # print(type(apparaat), end=", ") # returns <class 'Classes.Apparaten.Lamp'>
            # print(str(type(apparaat)).find("Lamp"), end=", ")
            # print(str(type(apparaat)).find("Deurslot"), end=", ")


            if str(type(apparaat)).find("Lamp") == 26:
                lamp:Lamp = apparaat

                lamp.statusAan = False
                lamp.verander_helderheid(0)

            elif str(type(apparaat)).find("Thermostaat") == 26:
                thermostaat:Thermostaat = apparaat

                thermostaat.statusAan = False
                thermostaat.verander_temperatuur(20)

            elif str(type(apparaat)).find("Deurslot") == 26:
                deurslot:Deurslot = apparaat

                deurslot.statusAan = True

            elif str(type(apparaat)).find("Beweging") == 26:
                bewegingssensor:Bewegingssensor = apparaat

                bewegingssensor.statusAan = False

            elif str(type(apparaat)).find("Rook") == 26:
                rookmelder:Rookmelder = apparaat

                # rookmelder.statusAan = False

            elif str(type(apparaat)).find("Gordijn") == 26:
                gordijn:Gordijn = apparaat

                gordijn.statusAan = False

            
        # print()