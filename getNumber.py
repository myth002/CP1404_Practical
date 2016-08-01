import string

def main():
    flag == False
    while flag == False:
        flag=get_number(10,50)

def get_number(lower,upper):
    a=int(input("Enter a number({:d}-{:d})").format(lower,upper))
    if (a<lower) or (a>upper):
        print("Please enter a valid number!")
        return False
    else:
        return True
main()