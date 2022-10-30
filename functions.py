from urllib.request import urlopen, Request
import json
import time
import random


def choice_vege(a):
    """Valitaan vihannes, käyttäjän valinnan mukaan

    Args:
        a (int): Valitaan vihannes taulukosta

    Returns:
        str: Valittu vihannes
    """
    vihannekset = ["Kurkku", "Tomaatti", "Porkkana", "Lanttu", "Retiisi"]
    return vihannekset[a]


def get_stats(valinta):
    """Hankkii halutun vihanneksen eli taistelijan tiedot ja tuo ne omiin muuttujiinsa.


    Args:
        valinta (str): Valittu vihannes

    Returns:
        Palauttaa taistelijan tiedot, pohjautuen Finelin tietolähteseen.
    """
    url = "https://fineli.fi/fineli/api/v1/foods?q={0}".format(valinta)
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    respo = urlopen(req)

    data = json.loads(respo.read())

    for i in data:
        if i["name"]["fi"] == valinta:
            energia = round(i["energyKcal"])
            hilarit = round(i["carbohydrate"], 1)
            protein = round(i["protein"], 1)
            rasva = round(i["fat"], 1)
            break
    return energia, hilarit, protein, rasva


def print_stats(
    valinta,
    valinta2,
    energia,
    hilarit,
    protein,
    rasva,
    energia1,
    hilarit1,
    protein1,
    rasva1,
    hitaus,
    hitaus1,
):
    """Tulostetaan taistelijoiden tiedot omiin lokeroihinsa"""
    print(
        "\n{0} \nEnergia {1} kcal \nHiilihydraatit {2} kcal \nProteiini {3} g \nRasva {4} g".format(
            valinta, energia, hilarit, protein, rasva
        )
    )

    print("")

    print(
        "Elämä {0} kcal \nHyökkäys {1} kcal \nPuolustus {2} g \nHitaus {3} g".format(
            energia, hilarit, protein, hitaus
        )
    )

    print("---------------------------")

    print(
        "{0} \nEnergia {1} kcal \nHiilihydraatit {2} kcal \nProteiini {3} g \nRasva {4} g".format(
            valinta2, energia1, hilarit1, protein1, rasva1
        )
    )

    print(" ")

    print(
        "Elämä {0} kcal \nHyökkäys {1} kcal \nPuolustus {2} g \nHitaus {3} g".format(
            energia1, hilarit1, protein1, hitaus1
        )
    )

    print("---------------------------")
    print("")

    print(
        "{0} VS {1}\n \x1B[3m{0} elämä: {2}, {1} elämä {3}\x1B[0m".format(
            valinta, valinta2, energia, energia1
        )
    )


def fight(valinta, valinta2, energia, energia1, hitaus, hitaus1):
    """Aloitetaan taistelu

    Returns:
        Taistelun kulku kerrottuna ja laskettuna
    """
    # Satunnaismuuttujat MoreHp ja KeppiStrike, tuodaan lisäjännitystä peliin
    # MoreHP = tuo 20 hptä lisää
    # KeppiStrike puolestaan lisää iskuvoimaa pysyvästi
    MoreHp = 20
    KeppiStrike = 5

    while energia > 0 and energia1 > 0:
        a = random.randint(0, 20)
        if a == 2:
            energia1 += MoreHp
            print(
                "{0} löysi energialähteen, hän sai {1} lisää elämää!".format(
                    valinta, MoreHp
                )
            )
        elif a == 17:
            hitaus += KeppiStrike
            print(
                "{0} löysi maasta kepin! Saa {1} lisää voimaa!".format(
                    valinta, KeppiStrike
                )
            )

        energia1 -= hitaus
        if energia1 < 0:
            energia1 = 0
        print(
            "{0} lyö ja tekee {1:.02f} vahinkoa. {2} jäi {3:.02f} elämää.".format(
                valinta, hitaus, valinta2, energia1
            )
        )
        if energia1 <= 0:
            break

        time.sleep(0.5)

        if a == 7:
            energia1 += MoreHp
            print(
                "{0} löysi energialähteen, hän sai {1} lisää elämää!".format(
                    valinta2, MoreHp
                )
            )
        elif a == 11:
            hitaus += KeppiStrike
            print(
                "{0} löysi maasta kepin! Saa {1} lisää voimaa!".format(
                    valinta, KeppiStrike
                )
            )

        energia -= hitaus1
        if energia < 0:
            energia = 0
        print(
            "{0} lyö ja tekee {1:.02f} vahinkoa. {2} jäi {3:.02f} elämää.".format(
                valinta2, hitaus1, valinta, energia
            )
        )

    return energia, energia1
