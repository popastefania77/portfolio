"""
CINEMATOGRAF (https://drive.google.com/file/d/11SaKuRYjz3ghhS6oOigt0EXLkF0ZgFXF/view?usp=drive_link)

Vă interesează în principal ca filmul pe care o să îl vizionați să înceapă cât mai repede din momentul în care
ajungeți la casa de bilete, iar, în cazul în care sunt mai multe filme care încep la ora dorită, să îl alegeți pe
cel cu prețul biletului cel mai mic.

CERINTA:
Selectati filmul care respectă cel mai bine dorințele voastre.

DATE DE INTRARE:
- hh:mm = ora la cre ajungeti la cinema
- n = numarul de oferte disponibile in programul cinematografului
- n linii = n filme (<oră> <preț> <nume film>)

DATE DE IESIRE:
- numele filmului ales

EXEMPLU:
22:00
4
17:00 15 Overlord
16:50 20 Morometii-2
23:05 13 Covorul-zburator
23:05 19 Bohemian-Rhapsody

Există două filme în program care încep la ora cea mai apropiată de cea de sosire, dar s-a ales filmul
“Covorul-zburator” deoarece prețul său, 13, este mai mic ca 19, prețul de la “Bohemian-Rhapsody”.
"""


#set 1 date de intrare
date_intrare = ['16:45', 4, ['18:00', 15, 'Bohemian-Rhapsody'], ['16:50', 20, 'Mos-Craciun-in-misiune'],
                ['12:00', 13, 'Creed-II'], ['16:55', 20, 'Grinch']]

#set 2 date de intrare
#date_intrare = ['22:00', 4, ['17:00', 15, 'Overlord'], ['16:50', 20, 'Morometii-2'],
#                ['23:05', 13, 'Covorul-zburator'], ['23:05', 19, 'Bohemian-Rhapsody']]


ora_curenta = date_intrare[0]  # ora la care se ajunge la cinema
print('Ora la care se ajunge la cinema :', ora_curenta)
n = date_intrare[1]
print('Numarul de filme disponibile :', n)

ora_minima = '24:59'  # initializez ora minima care o sa fie mai mare decat ora_curenta
ore = []  # initializez lista in care o sa pun toate orele
preturi = []  # initializez lista in care pun preturile
filme = []  # initializez lista in care pun numele filmelor
# pentru fiecare film
for i in range(n):
    ora, pret, film = date_intrare[i + 2]  # preiau ora, pretul si numele filmului
    # si le adaug la liste
    print(ora, film, pret)
    ore.append(ora)
    preturi.append(pret)
    filme.append(film)
    # aflu ora minima la care se poate intra la film, ulterioara orei curente
    if ora_minima > ora > ora_curenta:
        ora_minima = ora
        # pentru ora minima retin filmul
        nume_film = film

pret_minim = 100  # initializez pretul minim
if ore.count(ora_minima) != 1:  # daca ora minima este aceeasi pentru 2 sau mai multe filme
    # aflu pretul minim pentru aceste filme (care incep la aceeasi ora)
    for i in range(n):
        if ore[i] == ora_minima and pret_minim > preturi[i]:
            pret_minim = preturi[i]
            nume_film = filme[i]  # pentru pretul minim retin filmul

    print('\nFilmul care indeplineste conditiile :', nume_film)
else:
    print('\nFilmul care indeplineste conditiile :', nume_film)

"""
DATE DE INTRARE:
16:45
4
18:00 15 Bohemian-Rhapsody
16:50 20 Mos-Craciun-in-misiune
12:00 13 Creed-II
16:55 20 Grinch

DATE DE IESIRE:
Mos-Craciun-in-misiune


DATE DE INTRARE:
22:00
4
17:00 15 Overlord
16:50 20 Morometii-2
23:05 13 Covorul-zburator
23:05 19 Bohemian-Rhapsody

DATE DE IESIRE:
Covorul-zburator
"""
