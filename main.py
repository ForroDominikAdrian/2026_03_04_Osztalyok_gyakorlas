import random
from auto import Auto

auto1 = Auto("Toyota","Corolla",2015)
auto2 = Auto("Ford", "Focus", 2015)
auto3 = Auto("Suzuki","Swift",1998)
auto4 = Auto("Banán Autó","Spongyabob",2020)
auto4.gyorsit(9999999999999)
avg = 0
legidosebb = 0
legidosebb_auto = None
autok = [auto1,auto2,auto3]
for auto in autok:
    auto.gyorsit(random.randint(1,300))
    avg += 2026-auto.evjarat
    if legidosebb < auto.evjarat:
        legidosebb_auto = auto
        legidosebb = auto.evjarat
avg = avg/len(autok)
print(
      f"""
      Az autók átlagos évjárata: {round(avg,2)} év
      A legidősebb autó: {legidosebb_auto}
      """
      )




# autok = []

# with open("autok_lista.txt", "r", encoding="UTF-8") as forrasfajl:
#     for index, sor in enumerate(forrasfajl, start=1):
#         sor = sor.strip()
#         marka, tipus, evjarat = sor.split(";")

#         auto = Auto(
#             marka=marka,
#             tipus=tipus,
#             evjarat=int(evjarat)
#         )

#         autok.append(auto)