def addition(a, b):
    c = a + b
    return c

def subtraktion(a, b):
    d = a - b
    return d

a = float(input("Gib die erste Zahl ein: "))
b = float(input("Gib die zweite Zahl ein: "))

summe = addition(a, b)
differenz = subtraktion(a, b)

print("Die Summe ist", summe)
print("Die Differenz ist:", differenz)
