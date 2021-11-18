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
    print(sav)
        
        


kleurm(hvl)
