
rainy = "vihmane"
date_before_christmas = "20.12.2024"
date_in_autumn = "10.10.2025"


weather = input("Milline ilm on?")
date = input("Mis kuupaev tana on?")

if weather == "vihmane" and date == "date_before_christmas":
    print("Pole eriti talvine ilm, aga jalutada võib ikka")
elif weather == "vihamne" and date == "date_in_autumn":
    print("Ilus sügisilm, mine porilompi hüppama.")

    if weather == "vihmane":
        if date == "20.12.2024":
            print("Pole eriti talvine ilm, aga jalutada võib ikka")
        elif date == "10.10.2025":
            print("Ilus sügisilm, mine porilompi hüppama.")
