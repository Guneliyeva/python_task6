import random
import math

list = []

def myfunction():
    for i in (0, 5):
        num = random.randint(20, 50)
        list.append(num)
    print("Random ededlerin kvadratlari: ")
    for i in list:
        if i % 2 == 0:
            print(math.pow(i, 2))

myfunction()
