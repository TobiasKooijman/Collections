kleuren = ['oranje', 'blauw', 'groen', 'bruin']
import random
from random import randrange
hvl = input('Hoeveel kleuren moeten er toegevoegd worden? ')
def kleurm(hvl):
    for i in range(0,int(hvl)):
        num = random.randrange(0,4)
        print(kleuren[num])
        


kleurm(hvl)
