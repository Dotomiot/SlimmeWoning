# from .Classes.Apparaten import Apparaat,Bewegingssensor,Deurslot,Gordijn,Lamp,Rookmelder,Thermostaat
from Classes.Apparaten import *
from Classes.Bewoner import Bewoner
from Classes.Kamer import Kamer
from Classes.Smarthub import Smarthub
from Classes.Woning import Woning
from Classes.MQTT import MQTT_topic
import time

from logger import logger
from html_generator import maak_huisHTML, write_HTML

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

def smarthub():
    smarthub = Smarthub()
    return smarthub

def start_toestand():

    woning = Woning()
    woning.voeg_kamer_toe(woonkamer())
    woning.voeg_kamer_toe(keuken())
    woning.voeg_kamer_toe(slaapkamer1())
    woning.voeg_kamer_toe(slaapkamer2())
    woning.voeg_kamer_toe(badkamer())
    woning.voeg_kamer_toe(gang())
    woning.voeg_kamer_toe(smarthub())

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


def terminal_start():
    looping = True
    DEFAULT = 10

    print(f"Hoeveel stappen in de simulatie? (default={DEFAULT}) ('q' om te stoppen): ")

    while looping:
        answer = input()
        try:
            if answer == "":
                return DEFAULT
            
            elif answer == 'q' or answer == 'Q':
                print("Quit program early")
                return 0
            else:
                return int(answer)
        except:
            print(f"Geen getal, probeer opnieuw of 'q' om te stoppen" )


def main():
    AANTAL_STAPPEN = terminal_start()

    if AANTAL_STAPPEN == 0:
        return

    woning = start_toestand()
    # mane(woning)

    slimme = woning.smarthub

    MQTT_SLAAPKAMER1_SLOT = MQTT_topic("slimHuis/slaapkamer1/slot")
    MQTT_SLAAPKAMER1_TEMP = MQTT_topic("slimHuis/slaapkamer1/temp")

    MQTT_SLAAPKAMER1_SLOT.subscribe(slimme)
    MQTT_SLAAPKAMER1_TEMP.subscribe(slimme)

    warma = Thermostaat(32)

    MQTT_SLAAPKAMER1_TEMP.publish(warma.geef_temperatuur())
    print(slimme.subcribtions)
    MQTT_SLAAPKAMER1_TEMP.publish(warma.geef_temperatuur()+1)

    print(slimme.subcribtion_topic_list)
    print(slimme.subcribtions)

    bewoner_Tom = Bewoner("Tom")
    print(f"\n\n{bewoner_Tom.naam}:")
    for i in range(AANTAL_STAPPEN):
        # print(bewoner_Tom.beweeg_bewoner(woning.kamers), end="\t")
        bewoner_Tom.beweeg_bewoner(woning.kamers)
        print(f"\t============ Stap {i+1} ============\n")
        slimme.voer_regel_uit(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        logger(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        write_HTML(maak_huisHTML(woning))

        print()
        time.sleep(0.5)
    
if __name__ == "__main__":
    main()