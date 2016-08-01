def main():
    flag = False
    while flag == False:
        user_name = input("Enter your username: ")
        flag = nameCheck(user_name)

def nameCheck(name):
    count=0
    for pointer in range(0,len(name)):
        ref=name[pointer]
        count+=1
        if (pointer%2==1):
            print(ref)
    if count<1:
        return False
    else:
        return True
main()