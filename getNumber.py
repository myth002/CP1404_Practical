import string

def main():
    flag = False
    while flag == False:
        flag=get_number(10,50)

def get_number(lower,upper):
    a=int(input("Enter a number({:d} - {:d})\n>>>".format(lower,upper)))
    try:
        for x in range(0,len(a)):
            y = a[x]
            if y in string.digits:
                continue
    except:
        print("Please enter a valid number")
        return False
    if a<lower or a>upper:
        print("Please enter a valid number!")
        return False
    else:
         return True
main()