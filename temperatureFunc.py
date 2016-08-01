def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    choice="C"
    while choice.upper() != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice.upper()=="C":
            celsius = float(input("Celsius: "))
            tempCelc(celsius)
        elif choice.upper()=="F":
            farenheit = float(input("Farenheit: "))
            tempFare(farenheit)
        else:
            print("Invalid option")
    print("Thank you.")

def tempCelc(celsius):
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))

def tempFare(farenheit):
        celcius = 5/9*(farenheit-32)
        print("Result: {:.2f} F".format(celcius))

main()