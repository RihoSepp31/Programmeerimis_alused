# Funktsioon Celsiuse teisendamiseks Fahrenheiti
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Funktsioon Fahrenheiti teisendamiseks Celsiuseks
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Funktsioon Celsiuse teisendamiseks Kalviniks
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Funktsioon Kalvini teisendamiseks Celsiuseks
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Peamenüü funktsioon
def main_menu():
    while True:
        print("\nTere tulemast temperatuuri teisendajasse!")
        print("Vali:")
        print("1. Teisenda Celsiuse kraadid Fahrenheiti kraadideks")
        print("2. Teisenda Fahrenheiti kraadid Celsiuse kraadideks")
        print("3. Teisenda Celsiuse kraadid Kalviniteks")
        print("4. Teisenda Kalvini kraadid Celsiuseks")
        print("5. Välju programmist")

        choice = input("Sisesta oma valik (1, 2, 3, 4 või 5): ")

        if choice == "1":
            try:
                celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"Temperatuur Fahrenheiti kraadides on: {fahrenheit:.2f}")
            except ValueError:
                print("Palun sisesta kehtiv arv!")
        elif choice == "2":
            try:
                fahrenheit = float(input("Sisesta temperatuur Fahrenheiti kraadides: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"Temperatuur Celsiuse kraadides on: {celsius:.2f}")
            except ValueError:
                print("Palun sisesta kehtiv arv!")
        elif choice == "3":
            try:
                celsius = float(input("Sisesta temperatuur Celsiuse kraadides: "))
                kelvin = celsius_to_kelvin(celsius)
                print(f"Temperatuur Kalvinites on: {kelvin:.2f}")
            except ValueError:
                print("Palun sisesta kehtiv arv!")
        elif choice == "4":
            try:
                kelvin = float(input("Sisesta temperatuur Kalvinites: "))
                celsius = kelvin_to_celsius(kelvin)
                print(f"Temperatuur Celsiuse kraadides on: {celsius:.2f}")
            except ValueError:
                print("Palun sisesta kehtiv arv!")
        elif choice == "5":
            print("Head aega!")
            break
        else:
            print("Vale valik! Palun proovi uuesti.")

# Käivita programm
main_menu()
