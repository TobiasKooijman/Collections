kleuren = ['oranje', 'blauw', 'groen', 'bruin']
kleurendic = {
  "groen" : 2,
  "blauw" : 4,
  "oranje" : 5,
  "bruin" : 10
}

import random
from random import randrange
hvl = input('Hoeveel kleuren moeten er toegevoegd worden? ')
def kleurm(hvl):
    sav = 0
    for i in range(0,int(hvl)):
        num = random.randrange(0,4)
        kleurendic[kleuren[num]] += 1
        sav = kleurendic
    print("--------------")
    print("Gesorteerde M&M's:")
    print("")
    print("Groen: "+ str(sav["groen"]))
    print("Blauw: "+ str(sav["blauw"]))
    print("Oranje: "+str(sav["oranje"]))
    print("Bruin: "+str(sav["bruin"]))

kleurm(hvl)