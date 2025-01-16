'''
Väljasta ekraanile kõikvõimalikud kombinatsioonid kujul "x - y - z", kus x, y ja z on mistahes täisarvud 1-st 20-ni (20 kaasaarvatud).
Samuti loenda, mitu sellist kombinatsiooni leiti.
'''

counter = 0
for z in range (1,21):
    for y in range (1,21):
        for x in range(1,21):
            print(f"{x},{y}")
            counter += 1
print(f"{counter} kombinatsiooni")
