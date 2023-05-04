import random

Anzahl_Tipps = int(input("Anzahl der Lotto-Tipps: "))

Lottozahlen = list(range(1, 46))

for i in range(Anzahl_Tipps):
    tip = random.sample(Lottozahlen, 6)
    tip.sort()
    print(f"Tipp {i+1}: {tip}")