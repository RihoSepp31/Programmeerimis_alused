'''
On selge, et auto kiiruse tõstmine vähendab sõidule kuluvat aega ehk ma jõuame varem sihtpunkti.
Kui palju me aga ajas võidame? Koostage programm, mis küsib käivitamisel läbitava vahemaa pikkust (kilomeetrites, see kehtib kogu programmitöö aja),
seejärel aga küsib kasutajalt korduvalt kiirust (km/h) ning väljastab selle põhjal korrektse lausega sõiduks kuluva aja ja erinevuse eelmisest tulemusest.
Kui kasutaja uut kiirust ei sisesta, vaid vajutab lihtsalt sisestusklahvile, siis katkestatakse tsükkel ja tänatakse kasutajat.
'''

def calculate_time(distance, speed):
    """Arvutab sõiduks kuluva aja vastavalt kiirusele."""
    return distance / speed

def main():
    print("Tere tulemast sõiduaja kalkulaatorisse!")

    try:
        # Küsime vahemaa pikkuse
        distance = float(input("Sisestage läbitav vahemaa (km): "))
        if distance <= 0:
            print("Vahemaa peab olema suurem kui 0.")
            return
    except ValueError:
        print("Palun sisestage korrektne arv vahemaa pikkuseks.")
        return

    previous_time = None

    while True:
        try:
            # Küsime kasutajalt kiirust
            speed_input = input("Sisestage kiirus (km/h, Enter lõpetab): ")
            if not speed_input.strip():
                print("Aitäh kasutamast! Head teed!")
                break

            speed = float(speed_input)
            if speed <= 0:
                print("Kiirus peab olema suurem kui 0.")
                continue

            # Arvutame sõiduks kuluva aja
            time = calculate_time(distance, speed)

            # Väljastame sõiduaja ja erinevuse eelmisest tulemusest
            print(f"Kiirusel {speed} km/h kulub {time:.2f} tundi sihtpunkti jõudmiseks.")
            if previous_time is not None:
                time_difference = previous_time - time
                print(f"Võrreldes eelmise kiirusega säästate {time_difference:.2f} tundi.")

            previous_time = time

        except ValueError:
            print("Palun sisestage korrektne arv kiiruseks.")

if __name__ == "__main__":
    main()
