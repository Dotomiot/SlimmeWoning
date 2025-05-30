# from .Classes.Apparaten import Apparaat,Bewegingssensor,Deurslot,Gordijn,Lamp,Rookmelder,Thermostaat
from Classes.Apparaten import *
from Classes.Bewoner import Bewoner
from Classes.Kamer import Kamer
from Classes.Smarthub import Smarthub
from Classes.Woning import Woning


def woonkamer():
    lampje = Lamp(75)
    thermos = Thermostaat(22)
    beweger = Bewegingssensor()
    roker = Rookmelder()


    kamer = Kamer("woonkamer")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(thermos)
    kamer.voeg_apparaat_toe(beweger)
    kamer.voeg_apparaat_toe(roker)

    return kamer

def keuken():
    lampje = Lamp(80)
    thermos = Thermostaat(20)
    beweger = Bewegingssensor()

    kamer = Kamer("keuken")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(thermos)
    kamer.voeg_apparaat_toe(beweger)

    return kamer

def slaapkamer1():
    lampje = Lamp(30)
    slot = Deurslot(True)
    thermos = Thermostaat(20)
    beweger = Bewegingssensor()
    roker = Rookmelder()
    gordijn = Gordijn()

    kamer = Kamer("slaapkamer1")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(slot)
    kamer.voeg_apparaat_toe(thermos)
    kamer.voeg_apparaat_toe(beweger)
    kamer.voeg_apparaat_toe(roker)
    kamer.voeg_apparaat_toe(gordijn)

    return kamer

def slaapkamer2():
    lampje = Lamp(30)
    slot = Deurslot(True)
    thermos = Thermostaat(20)
    beweger = Bewegingssensor()
    roker = Rookmelder()
    gordijn = Gordijn()

    kamer = Kamer("slaapkamer2")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(slot)
    kamer.voeg_apparaat_toe(thermos)
    kamer.voeg_apparaat_toe(beweger)
    kamer.voeg_apparaat_toe(roker)
    kamer.voeg_apparaat_toe(gordijn)

    return kamer

def badkamer():
    lampje = Lamp(100)
    slot = Deurslot(False)
    thermos = Thermostaat(22)
    beweger = Bewegingssensor()

    kamer = Kamer("badkamer")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(slot)
    kamer.voeg_apparaat_toe(thermos)
    kamer.voeg_apparaat_toe(beweger)

    return kamer

def gang():
    lampje = Lamp(0)
    beweger = Bewegingssensor()
    roker = Rookmelder()

    kamer = Kamer("keuken")
    kamer.voeg_apparaat_toe(lampje)
    kamer.voeg_apparaat_toe(beweger)
    kamer.voeg_apparaat_toe(roker)

    return kamer

def start_toestand():

    woning = Woning()
    woning.voeg_kamer_toe(woonkamer())
    woning.voeg_kamer_toe(keuken())
    woning.voeg_kamer_toe(slaapkamer1())
    woning.voeg_kamer_toe(slaapkamer2())
    woning.voeg_kamer_toe(badkamer())
    woning.voeg_kamer_toe(gang())

    # for kamer in woning.kamers:
    #     print(kamer.naam)
    #     for apparaat in kamer.apparaten_lijst:
    #         print(f"\t {apparaat}")

    # print()
    # print(len(woning.kamers))
    # print(woning.kamers[0])
    # print(woning.kamers[2])


    return woning


def mane(woning: Woning):
    for kamer in woning.kamers:
        print(kamer.naam)
        for apparaat in kamer.apparaten_lijst:
            print(f"\t {apparaat}")

    print()
    print(len(woning.kamers))
    print(woning.kamers[0])
    print(woning.kamers[2])


def logger(woning, huidigeKamerInt, vorigeKamerInt):
    # for kamer in woning.kamers:
    #     print(kamer)
    #     for apparaat in kamer.apparaten_lijst:
    #         print(f"\t{str(type(apparaat))[26:-2]}: {apparaat}")

    # print()

    kamer: Kamer = woning.kamers[huidigeKamerInt]
    # print(kamer.naam)
    for apparaat in kamer.apparaten_lijst:
        # print(f"\t{str(type(apparaat))[26:-2]}: {apparaat}")

        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        print(f"\t{str(type(apparaat))[26:-2]} van {kamer} staat {status}")

    kamer: Kamer = woning.kamers[vorigeKamerInt]
    # print(kamer.naam)
    for apparaat in kamer.apparaten_lijst:
        # print(f"\t{str(type(apparaat))[26:-2]}: {apparaat}")

        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        print(f"\t{str(type(apparaat))[26:-2]} van {kamer} staat {status}")








if __name__ == "__main__":
    # main()
    woning = start_toestand()
    mane(woning)

    slimme = Smarthub()


    bewoner_Tom = Bewoner("Tom")
    print(f"\n\n{bewoner_Tom.naam}:")
    for i in range(2):
        # print(bewoner_Tom.beweeg_bewoner(woning.kamers), end="\t")
        slimme.voer_regel_uit(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        logger(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        print()
    