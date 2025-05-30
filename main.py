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
    woning.voeg_smarthub_toe(smarthub())

    return woning


def terminal_scenario():
    looping = True
    DEFAULT = "Normaal"

    print(f"Welk scenario?? (default={DEFAULT}): ")
    print(f"1: Normaal, 2: nacht, 3: vakantie")

    while looping:
        answer = input()
        try:
            answer = int(answer)
            if answer <=3 and answer >= 1:
                return answer
            else: 
                return 1
        except:
            return 1

def terminal_start():
    looping = True
    DEFAULT = 10

    print(f"Hoeveel stappen in de simulatie? (default={DEFAULT}) ('q' of 0 om te stoppen): ")

    while looping:
        answer = input()
        try:
            match answer:
                case "": return DEFAULT
                case "q": print("Quit program early"); return 0
                case "Q": print("Quit program early"); return 0
                case _: return int(answer)
        except:
            print(f"Geen getal, probeer opnieuw of 'q' om te stoppen" )


def example_subscriptions(woning: Woning):
    mqtt_test_topic = f"test/"
    for kamer in woning.kamers:
        mqtt_kamer_topic = mqtt_test_topic + f"{kamer}/"
        for apparaat in kamer.apparaten_lijst:
            mqtt_topic = mqtt_kamer_topic+f"{str(type(apparaat))[26:-2]}"
            mqtt = MQTT_topic(mqtt_topic)

            mqtt.subscribe(apparaat)
            mqtt.publish(f"{str(type(apparaat))[26:-2]}")


def list_all_mqtt_topics(woning: Woning):
    counter_topics = 0
    complete_topic_list = []
    for kamer in woning.kamers:
        for apparaat in kamer.apparaten_lijst:
            lijst = apparaat.subcribtion_topic_list
            if lijst == []:
                print("empty")
                continue
            else:
                for topic in lijst:
                    counter_topics += 1
                    print(f"{counter_topics}: {topic}")
                    complete_topic_list.append(topic)
    return complete_topic_list
    

def list_all_mqtt_data(woning: Woning, print_topics=True):
    complete_dictionary = {}
    for kamer in woning.kamers:
        for apparaat in kamer.apparaten_lijst:
            dicti = apparaat.subcribtions
            if dicti == {} and print_topics:
                print("empty")
                continue
            else:
                if print_topics:
                    print(dicti)
                complete_dictionary.update(dicti)
    return complete_dictionary

def publish_mqtt_topic_terminal(woning: Woning):
    topic_list = list_all_mqtt_topics(woning)
    topic_number = input(f"Kies een topic van de {len(topic_list)} topics: ")
    try:
        topic_number = int(topic_number)
    except:
        print("Not a number, so choosing 1")
        topic_number = 1
    print(topic_number)
    topic_str = topic_list[topic_number-1]
    print(topic_str)
    topic = MQTT_topic(topic_str)

    dictionary = list_all_mqtt_data(woning, False)
    print(dictionary[topic_str])
    
    data = input(f"Wat is de nieuwe data voor {topic_str}? ")
    topic.publish(data)

    dictionary = list_all_mqtt_data(woning, False)
    print(dictionary[topic_str])    # Data did not change, will fix later


def main():
    SCENARIO = terminal_scenario()

    if SCENARIO == 3:
        print("Er is geen gebruiker thuis, er is geen simulatie")
        print("Het programma sluit af")
        return
    

    AANTAL_STAPPEN = terminal_start()

    if AANTAL_STAPPEN == 0:
        return

    woning = start_toestand()

    slimme = woning.smarthub

    # voorbeelden van mogelijke subscriptions voor de smarthub in het MQTT systeem:

    # MQTT_SLAAPKAMER1_SLOT = MQTT_topic("slimHuis/slaapkamer1/slot")
    # MQTT_SLAAPKAMER1_TEMP = MQTT_topic("slimHuis/slaapkamer1/temp")

    # MQTT_SLAAPKAMER1_SLOT.subscribe(slimme)
    # MQTT_SLAAPKAMER1_TEMP.subscribe(slimme)

    # warma = Thermostaat(32)

    # MQTT_SLAAPKAMER1_TEMP.publish(warma.geef_temperatuur())
    # print(slimme.subcribtions)
    # MQTT_SLAAPKAMER1_TEMP.publish(warma.geef_temperatuur()+1)

    # print(slimme.subcribtion_topic_list)
    # print(slimme.subcribtions)

    example_subscriptions(woning)

    bewoner_Tom = Bewoner("Tom")

    for i in range(AANTAL_STAPPEN):

        answer = input("Press enter to take a step, 1 to view all the IOT data, 2 to publish to an MQTT topic: ")
        match answer:
            case "": print("Taking a step")
            case "1": list_all_mqtt_data(woning)
            case "2": publish_mqtt_topic_terminal(woning)
            case _: print("Not a good response, just taking a step"); 

        bewoner_Tom.beweeg_bewoner(woning.kamers)
        print(f"\t============ Stap {i+1} ============\n")
        slimme.voer_regel_uit(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt, SCENARIO)
        logger(woning, bewoner_Tom.huidigeKamerInt,bewoner_Tom.vorigeKamerInt)
        write_HTML(maak_huisHTML(woning))

        print()
    
if __name__ == "__main__":
    main()