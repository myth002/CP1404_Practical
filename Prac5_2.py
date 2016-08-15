#Pgm to output color codes based on keys using dictionaries

COLOR_NAME={"aliceblue": "#f0f8ff","antiquewhite": "#faebd7","beige": "#f5f5dc","black": "#000000","coral": "#ff7f50","darkgreen": "#006400","darkviolet": "#9400d3","greenyellow": "#adff2f","lavender": "#e6e6fa","magenta": "#ff00ff"}

user_choice = str(input("Enter color name: ")).lower()
while user_choice != "":
    if user_choice in COLOR_NAME:
        print(user_choice, "is", COLOR_NAME[user_choice])
    else:
        print("Invalid color name")
    user_choice = input("Enter color name: ").lower()

for user_choice in COLOR_NAME:
    print("{:4} is  {:20}".format(user_choice, COLOR_NAME[user_choice]))