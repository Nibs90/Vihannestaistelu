import functions

"""
    Vihannestaistelu - Solidabiksen koodihaaste
    (C) 2022 Jarno Heinonen
    email 90heinonen@gmail.com
"""
print(
    "Tervetuloa Vihannestaisteluun! \nAloitetaan valitsemalla kaksi taistelijaa. \nValitse numeroista 1-5 taistelijat: \n1:Kurkku \n2:Tomaatti \n3:Porkkana \n4:Lanttu \n5:Retiisi"
)

# Kysytään 1-5 valintaa, jolla valitaan haluttu taistelija
# Jatketaan niin kauan kunnes oikeanlaiset valinnat
while True:
    valinta1 = input("Syötä ensimmäinen vihannes: ")
    valinta2 = input("Syötä toinen vihannes: ")

    if valinta1.isdigit() and valinta2.isdigit() and 1 <= int(valinta1) <= 5 and 1 <= int(valinta2) <= 5:
        valinta1, valinta2 = int(valinta1) - 1, int(valinta2) - 1
        break
    print("Virheellinen arvo, arvon tulee olla 1-5 ja numeromuotoinen.")

# Muutetaan valintanumero vihannekseksi
vihannes1 = functions.choice_vege(valinta1)
vihannes2 = functions.choice_vege(valinta2)

# Haetaan vihannesten tiedot
energia, hilarit, protein, rasva = functions.get_stats(valinta)
energia1, hilarit1, protein1, rasva1 = functions.get_stats(valinta1)

hitaus = round((hilarit + protein + rasva), 1)
hitaus1 = round((hilarit1 + protein1 + rasva1), 1)

# Tulostetaan vihannesten tiedot
functions.print_stats(
    valinta,
    valinta1,
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
)

print("Taistelu alkakoot!")
hitaus -= protein1
hitaus1 -= protein

# Let the battle begins!
energia, energia1 = functions.fight(
    valinta, valinta1, energia, energia1, hitaus, hitaus1
)

# Tulostetaan voittaja f-stringin avulla
if energia > energia1:
    print(f"\n{vihannes1} voitti taistelun!")
else:
    print(f"\n{vihannes2} voitti taistelun!")
