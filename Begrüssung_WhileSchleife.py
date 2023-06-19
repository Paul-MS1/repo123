namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"]

def begruessung(name):
    print("Hallo", name)
    print("Schön dich zu sehen!")
    print("Viel Spaß mit dem Programm")

index = 0
while index < len(namen):
    begruessung(namen[index])
    index = index + 1
