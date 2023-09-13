"""
BOMBOANE (https://drive.google.com/file/d/1_FPvMbwCXj3Kytq9NiXZHK4u1y5EET1c/view?usp=drive_link)

În zona unde locuieşte Andrei există un singur magazin de bomboane, iar în fiecare zi se vinde un singur tip de
bomboană cu un anumit preţ şi o anumită aromă.
- Andrei cumpără bomboana într-o anumită zi dacă el are destui bani de la tatăl său şi acest lucru duce la
creşterea fericirii lui cu un anumit număr de puncte egal cu aroma bomboanei.
- Păstrează toţi banii rămaşi după ce a cumpărat bomboana pentru ziua urmatoare.
- Dacă nu are destui bani să îşi cumpere bomboana într-o anumită zi, punctele de fericire vor scădea doar dacă el
nu a cumpărat, în oricare din zilele  trecute, cel puţin o bomboană cu o aromă mai bună decât cea din ziua
curentă, pe care nu şi-o permite.

CERINTA:
Să se calculeze numărul de puncte de fericire al lui Andrei, care va creşte sau va scădea cu numărul pozitiv prin
care este reprezentată aroma. Presupunem că la început Andrei avea 0 lei şi 0 puncte de fericire.

DATE DE INTRARE:
- numărul întreg pozitiv n = numărul de zile în care băiatul primeşte bani de la tatăl său,
- n valori întregi pozitive = suma de bani pe care o primeşte băiatul in fiecare dintre cele n zile
- n linii = n perechi de numere întregi = costul şi aroma bomboanelor din magazin în fiecare zi.

DATE DE IESIRE:
- numărul de puncte de fericire pe care le are Andrei la finalul celor n zile (numar intreg)


EXEMPLU:
3
10 10 10
10 20
9 10
11 50

Andrei primeste bani de la tatal sau in 3 zile diferite:
In prima zi:
    - Andrei primeste 10 lei
    - bomboana costa 10 lei
    - cumpara bomboana => gradul de fericire creste la 20
    - ramane cu 0 lei
In a 2 - a zi:
    - Andrei primeste 10 lei
    - bomboana costa 9 lei
    - cumpara bomboana => gradul de fericire creste la 20 + 10 = 30
    - ramane cu 1 leu
In a 3 - a zi:
    - Andrei primeste 10 lei si are in total 10 + 1 = 11 lei
    - bomboana costa 11 lei
    - cumpara bomboana => gradul de fericire creste la 30 + 50 = 80

La finalul celor 3 zile, gradul de fericire al lui Andrei este 80 => se afiseaza 80

"""


#set 1 date de intrare
#date_intrare = [3, [10, 10, 10], [10, 20], [9, 10], [11, 50]]

#set 2 date de intrare
date_intrare = [4, [10, 10, 10, 4], [10, 20], [10, 10], [11, 50], [15, 10]]


n = date_intrare[0]
print('Numărul de zile în care băiatul primeşte bani de la tatăl său :', n)
lista_bani = date_intrare[1]  # banii pe care ii primeste in fiecare zi din cele n

grad_fericire = 0  # initializez gradul de fericire cu 0
print('Grad de fericire initial :', grad_fericire)
suma_bani = 0   # initializez suma de bani primita cu 0
print('Suma de bani initiala :', suma_bani)
# initializez aroma maxima cu 0 (o voi folosi pentru a afla care dintre arome are valoarea maxima)
aroma_maxima = 0
for i in range(n):
    print('Ziua', i + 1)
    # preiau din datele de intrare, pentru fiecare dintre cele n zile, costul bomboanei si aroma bomboanei
    # apare 2+ deoarece primele 2 elemente din lista sunt folosite
    cost_bomboana, aroma_bomboana = date_intrare[2 + i]
    print('Cost bomboana :', cost_bomboana)
    print('Aroma bomboana :', aroma_bomboana)
    suma_bani += lista_bani[i]  # lista_bani[i] = suma de bani corespunzatoare zilei i
    print('Suma de bani primita :', lista_bani[i])
    print('Suma de bani curenta :', suma_bani)

    if suma_bani >= cost_bomboana:  # daca ajung banii pentru a cumpara bomboana
        grad_fericire += aroma_bomboana  # gradul de fericire creste cu valoarea aromei bomboanei
        print('Grad de fericire curent :', grad_fericire)
        suma_bani -= cost_bomboana  # suma de bani scade cu valoarea costului bomboanei
        print('Suma de bani cu care a ramas dupa cumpararea bomboanei :', suma_bani)
        # aflu care dintrev arome este cea maxima
        if aroma_maxima < aroma_bomboana:
            aroma_maxima = aroma_bomboana
    else:  # daca nu ajung banii pentru cumpararea bomboanei
        if aroma_maxima < aroma_bomboana:  # daca baiatul nu a cumparat în oricare din zilele trecute cel puţin o
                                           # bomboană cu o aromă mai bună decât cea din ziua curentă
            grad_fericire -= aroma_bomboana  # gradul de fericire scade
            print('Grad de fericire curent :', grad_fericire)
            print('Suma de bani ramasa: ', suma_bani)
        else:
            print('Grad de fericire curent :', grad_fericire)
            print('Suma de bani ramasa: ', suma_bani)
print('\nGrad de fericire final:', grad_fericire)

"""
DATE DE INTRARE:
3
10 10 10
10 20
9 10
11 50

DATE DE IESIRE:
80


DATE DE INTRARE:
4
10 10 10 4
10 20
10 10
11 50
15 10

DATE DE IESIRE:
-20
"""

