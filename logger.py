from Classes.Kamer import Kamer
from datetime import date, time, datetime, timedelta

def logger(woning, huidigeKamerInt, vorigeKamerInt):

    nu = datetime.now()
    nu -= timedelta(microseconds=nu.microsecond)

    kamer: Kamer = woning.kamers[huidigeKamerInt]
    print(nu)
    print(f"\t{kamer.naam}:")

    for apparaat in kamer.apparaten_lijst:
        # print(f"\t{str(type(apparaat))[26:-2]}: {apparaat}")

        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        # print(f"\t\t{str(type(apparaat))[26:-2]} van {kamer} staat {status}")
        print(f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}")


    kamer: Kamer = woning.kamers[vorigeKamerInt]
    print(f"\t{kamer.naam}:")

    for apparaat in kamer.apparaten_lijst:
        # print(f"\t{str(type(apparaat))[26:-2]}: {apparaat}")

        if apparaat.statusAan:
            status = "aan"
        else:
            status = "uit"

        # print(f"\t\t{str(type(apparaat))[26:-2]} van {kamer} staat {status}")
        print(f"\t\t{str(type(apparaat))[26:-2]}\tstaat {status}")
