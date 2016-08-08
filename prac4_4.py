#pgm to generate a "quick pick" lottery pick

import random

def main():
    pickNum=[]
    num = int(input("Enter the number of quick picks: "))
    for x in range(0,num):
        pickNum=[]
        allowed_values=list(range(1,45))
        for y in range (0,6):
            pickNum.append(random.choice(allowed_values))
            allowed_values.remove(pickNum[y])
        pickNum.sort()
        print (pickNum)
main()