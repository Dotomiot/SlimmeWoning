from Classes.Kamer import Kamer
from datetime import date, time, datetime, timedelta

def logger(woning, huidigeKamerInt, vorigeKamerInt):
    nu = datetime.now()
    nu -= timedelta(microseconds=nu.microsecond)

    outputLogger = ""

    kamer: Kamer = woning.kamers[huidigeKamerInt]
    print(nu)
    print(f"\t{kamer.naam}:")

    for apparaat in kamer.apparaten_lijst:

        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        print(f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}")
        outputLogger += f"{kamer}: "
        outputLogger += f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}"
        outputLogger += ", "


    kamer: Kamer = woning.kamers[vorigeKamerInt]
    print(f"\t{kamer.naam}:")

    for apparaat in kamer.apparaten_lijst:
        
        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        print(f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}")
        outputLogger += f"{kamer}: "
        outputLogger += f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}"
        outputLogger += ", "

    
    file = open("logs.txt","a")
    file.write(f"{nu}\t{outputLogger}\n")
    file.close()

