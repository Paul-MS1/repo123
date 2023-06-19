deutsche_begriffe = ["Apfel", "Birne", "Marille", "Weintrauben", "Wassermelone"]
englische_begriffe = ["Apple", "Pear", "apricot", "grapes", "watermelon"]

deutscher_begriff = input("Geben Sie einen deutschen Begriff ein: ")

gefunden = False

for begriff in deutsche_begriffe:
    if begriff == deutscher_begriff:
        index = deutsche_begriffe.index(begriff)
        print("Der englische Begriff ist:", englische_begriffe[index])
        gefunden = True
        break

if not gefunden:
    print("Der deutsche Begriff ist nicht im Array enthalten.")
