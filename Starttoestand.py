# from .Classes.Apparaten import Apparaat,Bewegingssensor,Deurslot,Gordijn,Lamp,Rookmelder,Thermostaat
from Classes.Apparaten import *
from Classes.Bewoner import Bewoner
from Classes.Kamer import Kamer
from Classes.Smarthub import Smarthub
from Classes.Woning import Woning


def kamer1():
    lampje = Lamp(50)
    slot = Deurslot(True)

    kamer = Kamer("slaap")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(slot)

    return kamer

def kamer2():
    lampje = Lamp(100)
    slot = Deurslot(False)

    kamer = Kamer("bad")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(slot)

    return kamer

def kamer3():
    lampje = Lamp(0)

    kamer = Kamer("keuken")
    kamer.voeg_apparaat_toe(lampje)

    return kamer

def start_toestand():

    woning = Woning()
    woning.voeg_kamer_toe(kamer1())
    woning.voeg_kamer_toe(kamer2())
    woning.voeg_kamer_toe(kamer3())

    # for kamer in woning.kamers:
    #     print(kamer.naam)
    #     for apparaat in kamer.apparaten_lijst:
    #         print(f"\t {apparaat}")

    # print()
    # print(len(woning.kamers))
    # print(woning.kamers[0])
    # print(woning.kamers[2])


    return woning