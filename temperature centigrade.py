#Callum Brown
#30-09-14
#Temperature

temperature = int(input("Please enter the temperature in degrees centigrade: "))

if temperature > 100:
    print("The water is boiling")
elif temperature < 0:
    print("The water is frozen")
else:
    print("The water is neither")

