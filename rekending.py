listOne = (1,2,3,4,5,6,7,8,9,10)
listTwo = (2,4,6,8,10,12,14,16,18,20)
print("-----------------------------")
def addAndDisplayLists():
    print("Add List:")
    print("")
    for i in range(0,10):
        som = listOne[i] + listTwo[i]
        print(listOne[i], " + ", listTwo[i], " = ", som)

def substractAndDisplayLists():
    print("")
    print("Subtract List:")
    print("")
    for i in range(0,10):
        som = listOne[i] - listTwo[i]
        print(listOne[i], " - ", listTwo[i], " = ", som)

def multiplyAndDisplayLists():
    print("")
    print("Multiply List:")
    print("")
    for i in range(0,10):
        som = listOne[i] * listTwo[i]
        print(listOne[i], " X ", listTwo[i], " = ", som)

def divideAndDisplayLists():
    print("")
    print("Divide List:")
    print("")
    for i in range(0,10):
        som = listOne[i] / listTwo[i]
        print(listOne[i], " : ", listTwo[i], " = ", som)

addAndDisplayLists()
substractAndDisplayLists()
multiplyAndDisplayLists()
divideAndDisplayLists()