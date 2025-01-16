import summa


def solution():
    name = input("Sisesta nimi: ")
    for i in range(5):  # Indented appropriately within the function
        print(f"Ole tervitatud, {name}, {i + 1} korda!")


# Koosta programm, mis küsib kasutajalt 10 korda arve ja väljastab seejärel nende arvude summa.
# Täienda seda programmi nii, et kasutajalt küsitakse arve seni, kuni kasutaja enam uut arvu ei sisesta,
# vaid vajutab lihtsalt sisestusklahvi. Proovige seda ülesannet lahendada nii while- kui for-tsükliga.


def sum_unlimited():
    counter = 0
    total = 0
    while True:
        counter += 1
        user_input = input(f"Sisesta {counter}. täisarv: ")
        if user_input == "":
            break
        user_number = int(user_input)
        total += user_number
        # TODO katkesta sukkel teatud juhul
        total += user_number
    print(f"Sisestatud {counter} arvu summa  on: {total}")


'''
Koosta programm,
mis aitab lastel treenida liitmist. Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust. Kui vastus on õige,
kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte. Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10),
samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50). Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast
viimast tehet tulemuse.
'''


from random import randint

def practice_adding(lowest=1,highest=50,count=10):
    correct_answers = 0
    for i in range(count):
        first_number = randint(lowest, highest)
        second_number = randint(lowest, highest)
        user_answer = int(input(f"{first_number} + {second_number} = ? "))
        if user_answer == first_number + second_number:
            correct_answers += 1
            print("CORRECT! very smart!")
            correct_answers += 1
        else:
            print("Room for improvement!")
            print(f"{first_number} + {second_number} = {first_number + second_number} = {correct_answers}")

        print(f"You tried {count} times and got the answer correct {correct_answers} times.")





if __name__== '__main__':
    practice_adding()

