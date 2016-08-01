def main():
    a = fix_score()
    print(a)

def fix_score():
    score = float(input("Enter score: "))
    if score<0 or score>100:
        return("Invalid score")
    elif score>90:
        return("Excellent")
    elif score > 50:
        return("Passable")
    else:
        return("Bad")

main()