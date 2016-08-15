#Pgm to test occurences of a word in a string using dictionaries

def main():
    user_str=input("Enter a string: ")
    test=user_str.split()
    count_dict={}
    for x in test:
        if x in count_dict:
            count_dict[x]+=1
        else:
            count_dict[x]=1
    for key,value in count_dict.items():
        print("{:s} : {:d}".format(str(key),int(value)))

main()