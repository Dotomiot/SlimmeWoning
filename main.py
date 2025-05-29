# from .Classes.Apparaten import Apparaat,Bewegingssensor,Deurslot,Gordijn,Lamp,Rookmelder,Thermostaat
from Classes.Apparaten import *
from Classes.Bewoner import Bewoner
from Classes.Kamer import Kamer
from Classes.Smarthub import Smarthub
from Classes.Woning import Woning

from Starttoestand import start_toestand



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

    print(f"\n\nTom:")

    bewoner_Tom = Bewoner("Tom")
    # kamer
    for i in range(2):
        # print(bewoner_Tom.beweeg_bewoner(woning.kamers), end="\t")
        slimme.voer_regel_uit(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        logger(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        print()
    