# python igra - pogodii broj

import random

tajnibroj = random.randint(1,30)

while True:

        pogodi = int(input("Pogodi broj između 1 i 30:"))

        if pogodi == tajnibroj:
                print("Bravo pogodio si traženi broj!")
                break
        elif pogodi > tajnibroj:
                print("pogriješio si pokušaj manji broj:")
        elif pogodi < tajnibroj:
                print("pogrješio si, pokušaj veći broj")
        else:
                print("Pogriješio i, pokušaj ponovo...")