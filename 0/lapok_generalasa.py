# Projekt: HTML_GENERATOR
# Author:  zavorszky@yahoo.com
# Task:    HTML kód generálás.
#          Egy speciális feladathoz HTML dokumentumok vagy
#          dokumentum részek készítése.

# A HTML lapok generálásához szükséges adatok.
# Figyelem!
# A program logikába be van építve a "napló" projekt lapjainak
# felépítése és kapcsolatai. A program egy vázat generál.
# A TARTALMAT a napló írónak kell a vázra építeni.

adatok = {
    "kozos": {
        "lang": "hu-HU",
        "stylesheets": [
            "resources/css/naplo.css"
        ]
    },
    "lapok":[
        {
            "nev": "index",
            "file_nev": "index.html",
            "title_tag": "index",
        }
    ],
    "lap_kapcsolatok": [
        "index"
    ]

}


# def htmlTag(tagNev, tagTulajdonság, tartalom):
#    if tagTulajdonság == "":
#        return f"\n<{tagNev}>{tartalom}\n</{tagNev}>"
#    return f"<{tagNev} {tagTulajdonság}>{tartalom}\n</{tagNev}>"


def htmlTag(tagNev, tagTulajdonsagok, tartalom, kellTagZaras=True):
    tag = "\n<" + tagNev
    for tulajdonsag in tagTulajdonsagok:
        tag += " " + tulajdonsag
    tag += ">"
    if kellTagZaras:
        tag += tartalom
        tag += "\n</" + tagNev + ">"
    return tag


def lapok_generalasa():
    v_tulLang = f'lang="{adatok["kozos"]["lang"]}"'
    for lap in adatok["lapok"]:
        lapNev = lap["nev"]
        
        print(
            htmlTag(
                "html",
                [
                    v_tulLang,
                ],
                htmlTag("head", [], htmlTag("title",[], lapNev) +
                        htmlTag("meta", ['charset="UTF-8"'], "", False)+
                        htmlTag("meta", ['name="viewport"', 'content="width=device-width, initial-scale=1.0"'],"", False)+
                        htmlTag("link",['rel="stylesheet"' 'href="resources/css/naplo.css"'], "", False)) 
                + htmlTag("body", [], htmlTag("p", [], "Hello!")),
            )
        )


lapok_generalasa()
