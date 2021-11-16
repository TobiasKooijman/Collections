spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']
import random
from random import randrange

def spelProgramma(lijst,mini,maxi):
    print("------------------------------------------")
    print("Lijst van spellen:")
    print("")
    for i in range(random.randrange(mini,maxi)):
        num = random.randrange(0,len(lijst))
        print(lijst[num])
    
    
spelProgramma(spelList,3,10)