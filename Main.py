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
    nro = input("Syötä eka vihannes ")
    nro1 = input("Syötä toka vihannes ")
    if nro in map(str, range(1, 6)) and nro1 in map(str, range(1, 6)):
        nro = int(nro) - 1
        nro1 = int(nro1) - 1
        break
    print("Väärä arvo, arvon tulee olla 1-5")

# Muutetaan valintanumero vihannekseksi
valinta = functions.choice_vege(nro)
valinta1 = functions.choice_vege(nro1)

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

# Selvitetään voittaja
if energia > energia1:
    print("\n{0} voitti taistelun!".format(valinta))
else:
    print("\n{0} voitti taistelun!".format(valinta1))
