print("UNIT CONVERTER TOOL")

print("1. Kilometers to Miles")
print("2. Celsius to Fahrenheit")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    km = float(input("Enter kilometers: "))
    miles = km * 0.621371
    print("Miles:", miles)

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", fahrenheit)

else:
    print("Invalid choice")