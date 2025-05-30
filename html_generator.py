from Classes.Woning import Woning

def maak_huisHTML(woning: Woning):
    returnHTML = f"<h1>{woning.naam}</h1>"

    for kamer in woning.kamers:
        # print(kamer.naam)
        returnHTML += f"<ul><h2>{kamer.naam}</h2>"
        for apparaat in kamer.apparaten_lijst:
            # print(f"\t {apparaat}")
            returnHTML += f"<li>{str(type(apparaat))[26:-2]}: {apparaat.statusAan}</li>"
        returnHTML += f"</ul>"

    returnHTML = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Slimme woning simulatie</title>
    </head>
    <body>
        <ul id="floorplan">{returnHTML}
        </ul>
    </body>
    </html>
    """

    return returnHTML

def write_HTML(HTML,file="huis.html"):
    file = open("_site/huis.html", "w")
    file.write(HTML)
    file.close()