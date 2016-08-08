#Pgm to find min, max, sum and len

def main():
    numbers=[]
    for x in range (0,5):
        u=int(input("Number: "))
        numbers.append(u)
    print("The first number is {:d}".format(numbers[0]))
    print("The last number is {:d}".format(numbers[4]))
    print("The smallest number is {:d}".format(min(numbers)))
    print("The largest number is {:d}".format(max(numbers)))
    print("The average of the numbers is {:.2f}".format(sum(numbers)/len(numbers)))

main()