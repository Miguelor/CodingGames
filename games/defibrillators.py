#3,879483
#43,608177
#3
#1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217
#2;Hotel de Ville;1 place Georges Freche 34267 Montpellier;;3,89652239197876;43,5987299452849
#3;Zoo de Lunaret;50 avenue Agropolis 34090 Mtp;;3,87388031141133;43,6395872778854

import math

to_float = lambda x: float(x.replace(",", "."))

lon = to_float(input())
lat = to_float(input())

n = int(input())
defibs = list()
min_dist = float("inf")

for i in range(n):
    defib = input().split(";")

    lonB = to_float(defib[4])
    latB = to_float(defib[5])
    
    x = (lonB - lon) * math.cos((lat + latB)/2)
    y = latB - lat
    d = math.sqrt(x**2 + y**2) * 6371
    if d < min_dist : best, min_dist = defib[1], d

print(best)